"""확장 실습: 반복 배치, 준비도 진단, 다중 장비 상태, 가상 온도장.

모든 센서 값과 온도장은 교육용 합성 데이터이며 실제 CAE/장비 측정값이 아니다.
"""
import csv
import math
from pathlib import Path
from pxr import Usd, UsdGeom, UsdPhysics, Sdf, Gf, Vt
from cbnu_lab import ROOT
from telemetry import classify

EQUIPMENT_IDS = ("E01", "E02", "E03")
STATE_COLORS = {"UNKNOWN": (0.45, 0.45, 0.45), "STALE": (0.3, 0.4, 0.55)}

def cube(stage, path, position, scale, color):
    obj = UsdGeom.Cube.Define(stage, path)
    obj.CreateSizeAttr(1)
    xf = UsdGeom.XformCommonAPI(obj)
    xf.SetTranslate(Gf.Vec3d(*position))
    xf.SetScale(Gf.Vec3f(*scale))
    obj.CreateDisplayColorAttr(Vt.Vec3fArray([Gf.Vec3f(*color)]))
    return obj.GetPrim()

def batch_parts(stage, rows=2, columns=3, spacing=0.45):
    if not isinstance(rows, int) or not isinstance(columns, int) or not (1 <= rows <= 5 and 1 <= columns <= 5):
        raise ValueError("rows, columns는 1~5 정수입니다.")
    if not math.isfinite(spacing) or spacing < 0.25:
        raise ValueError("spacing은 0.25m 이상이어야 합니다.")
    base = "/World/Batch"
    # 교육 전용 경로만 교체하여 반복 실행 시 이전 배열이 남지 않게 한다.
    if stage.GetPrimAtPath(base):
        stage.RemovePrim(base)
    UsdGeom.Xform.Define(stage, base)
    paths = []
    for row in range(rows):
        for column in range(columns):
            path = f"{base}/Part_{row:02d}_{column:02d}"
            p = cube(stage, path, (0.5 + column*spacing, -1.5 + row*spacing, 0.1),
                     (0.2,0.2,0.2), (0.2,0.55,0.85))
            p.CreateAttribute("training:part_id", Sdf.ValueTypeNames.String).Set(f"P{row*columns+column+1:03d}")
            paths.append(path)
    return paths

def readiness(stage):
    """본 과정에서 정한 낙하 실험 준비 조건. 일반 SimReady 인증기가 아니다."""
    obj = stage.GetPrimAtPath("/World/Workpiece")
    floor = stage.GetPrimAtPath("/World/Ground")
    eq = stage.GetPrimAtPath("/World/Equipment")
    bounds = UsdGeom.BBoxCache(Usd.TimeCode.Default(), ["default", "render"])
    height = bounds.ComputeWorldBound(eq).ComputeAlignedRange().GetSize()[2] if eq else 0
    mass = obj.GetAttribute("physics:mass").Get() if obj else None
    enabled = obj.GetAttribute("physics:rigidBodyEnabled").Get() if obj else None
    checks = [
        ("meter/Z-up", UsdGeom.GetStageMetersPerUnit(stage)==1 and UsdGeom.GetStageUpAxis(stage)=="Z"),
        ("equipment_height_1_to_3m", 1 < height < 3),
        ("physics_scene", bool(stage.GetPrimAtPath("/World/PhysicsScene"))),
        ("workpiece_collider", bool(obj and obj.HasAPI(UsdPhysics.CollisionAPI))),
        ("workpiece_rigid_body", bool(obj and obj.HasAPI(UsdPhysics.RigidBodyAPI) and enabled is not False)),
        ("positive_mass", mass is not None and math.isfinite(mass) and mass>0),
        ("ground_collider", bool(floor and floor.HasAPI(UsdPhysics.CollisionAPI) and
                                 floor.GetAttribute("physics:collisionEnabled").Get() is not False)),
    ]
    return checks

def read_multi(path, max_age_s=3):
    if not math.isfinite(max_age_s) or max_age_s < 0:
        raise ValueError("max_age_s >= 0 이어야 합니다.")
    groups, seen = {}, set()
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            now, sample = float(row["time_s"]), float(row["sample_time_s"])
            key = row["equipment_id"]
            if key not in EQUIPMENT_IDS or not math.isfinite(now) or not math.isfinite(sample) or not 0 <= sample <= now:
                raise ValueError("장비 ID 또는 시각이 올바르지 않습니다.")
            if (now,key) in seen:
                raise ValueError("동일 시각과 장비의 중복 행입니다.")
            seen.add((now,key))
            temp = float(row["temperature_c"]) if row["temperature_c"].strip() else None
            vib = float(row["vibration_mm_s"]) if row["vibration_mm_s"].strip() else None
            if temp is not None and not math.isfinite(temp):
                raise ValueError("온도는 유한한 수여야 합니다.")
            if vib is not None and (not math.isfinite(vib) or vib<0):
                raise ValueError("진동은 유한한 0 이상 수여야 합니다.")
            if temp is None or vib is None:
                state,color = "UNKNOWN",STATE_COLORS["UNKNOWN"]
            elif now-sample > max_age_s:
                state,color = "STALE",STATE_COLORS["STALE"]
            else:
                state,color = classify(temp,vib)
            groups.setdefault(now,[]).append(dict(time_s=now, equipment_id=key, temperature_c=temp,
                vibration_mm_s=vib, sample_time_s=sample, state=state, color=color))
    if not groups:
        raise ValueError("CSV가 비어 있습니다.")
    for now, rows in groups.items():
        if {r["equipment_id"] for r in rows} != set(EQUIPMENT_IDS):
            raise ValueError(f"{now}초에 E01/E02/E03 행이 모두 필요합니다. 결측은 빈 값으로 표시하세요.")
    return [(now, sorted(rows,key=lambda r:r["equipment_id"])) for now,rows in sorted(groups.items())]

def apply_multi(stage, rows):
    for row in rows:
        p = stage.GetPrimAtPath(f"/World/Stations/{row['equipment_id']}")
        if not p:
            raise ValueError("08_multi_equipment.usda를 먼저 여세요.")
        lamp = UsdGeom.Sphere(stage.GetPrimAtPath(str(p.GetPath())+"/Lamp"))
        lamp.CreateDisplayColorAttr(Vt.Vec3fArray([Gf.Vec3f(*row["color"])]))
        for key in ("state","equipment_id"):
            p.CreateAttribute("training:"+key,Sdf.ValueTypeNames.String).Set(row[key])
        p.CreateAttribute("training:source",Sdf.ValueTypeNames.String).Set("SYNTHETIC_MULTI_CSV")
        for key in ("time_s","sample_time_s","temperature_c","vibration_mm_s"):
            attr=p.CreateAttribute("training:"+key,Sdf.ValueTypeNames.Double)
            if row[key] is None:
                attr.Block()  # 이전 수치가 정상 데이터처럼 남지 않도록 한다.
            else:
                attr.Set(row[key])

def thermal_colors(values, low=20, high=100):
    if not math.isfinite(low) or not math.isfinite(high) or high <= low:
        raise ValueError("범례 상한은 하한보다 커야 합니다.")
    colors=[]
    for value in values:
        if not math.isfinite(value):
            raise ValueError("온도는 유한한 수여야 합니다.")
        t=max(0,min(1,(value-low)/(high-low)))
        colors.append(Gf.Vec3f(t,0.25,1-t))
    return Vt.Vec3fArray(colors)

def apply_thermal(stage, csv_path, low=20, high=100):
    mesh=UsdGeom.Mesh(stage.GetPrimAtPath("/World/ThermalPlate"))
    if not mesh:
        raise ValueError("09_thermal_field.usda를 먼저 여세요.")
    with Path(csv_path).open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    values={}
    for row in rows:
        idx=int(row["face_id"])
        if idx in values:
            raise ValueError("중복 face_id")
        values[idx]=float(row["temperature_c"])
    count=len(mesh.GetFaceVertexCountsAttr().Get())
    if set(values) != set(range(count)):
        raise ValueError("face_id는 Mesh 면 수와 정확히 일치해야 합니다.")
    ordered=[values[i] for i in range(count)]
    colors=thermal_colors(ordered,low,high)
    pv=mesh.CreateDisplayColorPrimvar(UsdGeom.Tokens.uniform)
    pv.Set(colors)
    mesh.GetPrim().CreateAttribute("training:temperature_c",Sdf.ValueTypeNames.FloatArray).Set(ordered)
    mesh.GetPrim().CreateAttribute("training:legend_min_c",Sdf.ValueTypeNames.Float).Set(low)
    mesh.GetPrim().CreateAttribute("training:legend_max_c",Sdf.ValueTypeNames.Float).Set(high)
    mesh.GetPrim().CreateAttribute("training:source",Sdf.ValueTypeNames.String).Set("SYNTHETIC_FIELD_NOT_CAE")
    return min(ordered),max(ordered)
