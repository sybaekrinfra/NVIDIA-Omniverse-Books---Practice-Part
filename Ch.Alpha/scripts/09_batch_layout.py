"""Script Editor에서 이 파일 전체를 실행하세요. 초기화 스크립트가 필요 없습니다."""

def main():
    import math
    import omni.usd
    import omni.timeline
    from pxr import UsdGeom, Sdf, Gf, Vt
    TARGET = "/World/Workpiece"

    def cube(stage, path, position, scale, color):
        obj = UsdGeom.Cube.Define(stage, path)
        obj.GetPrim().SetActive(True)
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
            for child in list(stage.GetPrimAtPath(base).GetChildren()):
                path = child.GetPath()
                stage.RemovePrim(path)
                remaining = stage.GetPrimAtPath(path)
                if remaining:
                    remaining.SetActive(False)  # 약한 Layer의 물체도 숨깁니다.
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

    assert omni.timeline.get_timeline_interface().is_stopped(), "Stop 후 실행하세요."
    s=omni.usd.get_context().get_stage()
    assert s, "실습 장면을 먼저 여세요."
    assert s.GetPrimAtPath("/World/Batch"), "07_batch_layout.usda를 여세요."
    ROWS=2
    COLUMNS=3
    SPACING_M=0.45
    paths=batch_parts(s,ROWS,COLUMNS,SPACING_M)
    print("작업물 수:",len(paths))
    print("\n".join(paths))


main()
