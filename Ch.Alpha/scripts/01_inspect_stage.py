"""Script Editor에서 이 파일 전체를 실행하세요. 초기화 스크립트가 필요 없습니다."""

def main():
    import omni.usd
    import omni.timeline
    from pxr import Usd, UsdGeom
    TARGET = "/World/Workpiece"
    def current_stage():
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


    inspect(current_stage())


main()
