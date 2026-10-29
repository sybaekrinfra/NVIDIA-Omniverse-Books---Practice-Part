"""Kit Script Editor와 오프라인 USD 검증이 공유하는 수업 함수."""
from pathlib import Path
from pxr import Usd, UsdGeom, UsdPhysics, Sdf, Gf, Vt
from telemetry import read_samples

ROOT = Path(__file__).resolve().parents[2]
TARGET = "/World/Workpiece"

def current_stage():
    import omni.usd
    stage = omni.usd.get_context().get_stage()
    if not stage or not stage.GetPrimAtPath("/World/StatusLamp") or not stage.GetPrimAtPath(TARGET):
        raise RuntimeError("checkpoints 폴더의 교육 장면을 먼저 여세요.")
    return stage

def inspect(stage):
    print("unit(m):", UsdGeom.GetStageMetersPerUnit(stage), "up:", UsdGeom.GetStageUpAxis(stage))
    for path in ["/World", "/World/Equipment", TARGET, "/World/StatusLamp"]:
        p = stage.GetPrimAtPath(path)
        print(path, p.GetTypeName() if p else "MISSING")
    box = UsdGeom.BBoxCache(Usd.TimeCode.Default(), ["default", "render"])
    print("Equipment bound:", box.ComputeWorldBound(stage.GetPrimAtPath("/World/Equipment")).ComputeAlignedRange())

def add_physics(stage):
    """단순 Cube만 동적 강체로 설정. CAD 장비는 시각 참조용."""
    if UsdGeom.GetStageMetersPerUnit(stage) != 1 or UsdGeom.GetStageUpAxis(stage) != "Z":
        raise ValueError("본 실습은 meter / Z-up 기준입니다.")
    scene = UsdPhysics.Scene.Define(stage, "/World/PhysicsScene")
    scene.CreateGravityDirectionAttr(Gf.Vec3f(0, 0, -1))
    scene.CreateGravityMagnitudeAttr(9.81)
    floor = stage.GetPrimAtPath("/World/Ground")
    obj = stage.GetPrimAtPath(TARGET)
    if not floor or not obj:
        raise ValueError("Ground와 Workpiece가 필요합니다.")
    UsdPhysics.CollisionAPI.Apply(floor)
    UsdPhysics.CollisionAPI.Apply(obj)
    body = UsdPhysics.RigidBodyAPI.Apply(obj)
    body.CreateRigidBodyEnabledAttr(True)
    body.CreateKinematicEnabledAttr(False)
    UsdPhysics.MassAPI.Apply(obj).CreateMassAttr(1.0)
    print("Physics: gravity 9.81 m/s², Workpiece mass 1 kg")

def set_workpiece(stage, height=1.5, mass=1.0):
    if height < 0.1 or mass <= 0:
        raise ValueError("height >= 0.1 m, mass > 0 kg 조건을 지키세요.")
    p = stage.GetPrimAtPath(TARGET)
    # 준비된 단일 translate op만 변경하여 복잡한 CAD transform을 보존한다.
    p.GetAttribute("xformOp:translate").Set(Gf.Vec3d(1, 0, height))
    UsdPhysics.MassAPI.Apply(p).CreateMassAttr(mass)
    print("height(m)=", height, "mass(kg)=", mass)

def apply_sample(stage, sample):
    sec, t, v, state, color = sample
    lamp = UsdGeom.Sphere(stage.GetPrimAtPath("/World/StatusLamp"))
    lamp.CreateDisplayColorAttr(Vt.Vec3fArray([Gf.Vec3f(*color)]))
    p = stage.GetPrimAtPath("/World/Equipment")
    for name, typ, value in [
        ("training:time_s", Sdf.ValueTypeNames.Double, sec),
        ("training:temperature_c", Sdf.ValueTypeNames.Float, t),
        ("training:vibration_mm_s", Sdf.ValueTypeNames.Float, v),
        ("training:state", Sdf.ValueTypeNames.String, state),
        ("training:source", Sdf.ValueTypeNames.String, "SYNTHETIC_CSV"),
    ]:
        p.CreateAttribute(name, typ, custom=True).Set(value)
    print(f"{sec:4.1f}s {t:4.1f}°C {v:3.1f}mm/s {state}")

def save_result(stage, name):
    if Path(name).name != name or not name.endswith(".usda"):
        raise ValueError("파일 이름만 지정하세요. 확장자는 .usda입니다.")
    dest = ROOT / "outputs" / name
    dest.parent.mkdir(exist_ok=True)
    # 상대 경로 유실을 방지하는 단일 파일 제출본. 원래 composition은 checkpoints에 보존.
    # Python 파일 쓰기로 Windows USD writer의 비ASCII 경로 문제를 피한다.
    dest.write_text(stage.Flatten().ExportToString(), encoding="utf-8")
    print("Saved flattened submission:", dest)
    return dest

def samples():
    return read_samples(ROOT / "shared/data/equipment_status.csv")
