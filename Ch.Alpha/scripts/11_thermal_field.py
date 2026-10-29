"""Script Editor에서 이 파일 전체를 실행하세요. 초기화 스크립트가 필요 없습니다."""

def main():
    from pathlib import Path
    import math
    import csv
    import omni.usd
    import omni.timeline
    from pxr import UsdGeom, Sdf, Gf, Vt
    # CSV・저장 경로. 자동 탐색 실패 시에만 아래 값을 수정하세요.
    ROOT = None  # 예: Path(r"C:/omniverse/Ch.Alpha")
    if ROOT is None:
        opened_stage = omni.usd.get_context().get_stage()
        file_path = opened_stage.GetRootLayer().realPath if opened_stage else ""
        ROOT = next((p for p in Path(file_path).parents
                     if (p / "checkpoints").is_dir() and (p / "shared/data").is_dir()), None) if file_path else None
    if ROOT is None:
        raise RuntimeError("Ch.Alpha의 장면을 열거나 이 파일의 ROOT를 지정하세요.")
    ROOT = Path(ROOT).expanduser().resolve()
    if not (ROOT / "shared/data").is_dir():
        raise RuntimeError("ROOT는 shared/data를 포함한 Ch.Alpha 폴더여야 합니다.")
    TARGET = "/World/Workpiece"

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

    s=omni.usd.get_context().get_stage()
    assert s, "실습 장면을 먼저 여세요."
    DATASET="thermal_hotspot.csv"  # thermal_baseline.csv / thermal_hotspot.csv
    LEGEND_MIN_C=20
    LEGEND_MAX_C=100
    assert DATASET in ("thermal_baseline.csv","thermal_hotspot.csv")
    print("가상 온도 범위:",apply_thermal(s,ROOT/"shared/data"/DATASET,LEGEND_MIN_C,LEGEND_MAX_C))
    print("교육용 합성 분포입니다. CAE 해석 결과가 아닙니다.")


main()
