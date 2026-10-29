"""Script Editor에서 이 파일 전체를 실행하세요. 초기화 스크립트가 필요 없습니다."""

def main():
    import math
    import omni.usd
    import omni.timeline
    from pxr import UsdPhysics, Gf
    TARGET = "/World/Workpiece"
    def current_stage():
        stage = omni.usd.get_context().get_stage()
        if not stage or not stage.GetPrimAtPath("/World/StatusLamp") or not stage.GetPrimAtPath(TARGET):
            raise RuntimeError("checkpoints 폴더의 교육 장면을 먼저 여세요.")
        return stage

    def set_workpiece(stage, height=1.5, mass=1.0):
        if not math.isfinite(height) or not math.isfinite(mass) or height < 0.1 or mass <= 0:
            raise ValueError("height >= 0.1 m, mass > 0 kg 조건을 지키세요.")
        p = stage.GetPrimAtPath(TARGET)
        # 준비된 단일 translate op만 변경하여 복잡한 CAD transform을 보존한다.
        position_attr = p.GetAttribute("xformOp:translate")
        position = position_attr.Get()
        if position is None:
            raise ValueError("Workpiece에 translate 속성이 필요합니다.")
        position_attr.Set(Gf.Vec3d(position[0], position[1], height))
        UsdPhysics.MassAPI.Apply(p).CreateMassAttr(mass)
        print("height(m)=", height, "mass(kg)=", mass)


    assert omni.timeline.get_timeline_interface().is_stopped(), "Stop 버튼을 누르세요."

    # 학습자 변경 지점: 먼저 높이만 바꾸고 다음에 질량을 바꾸세요.
    HEIGHT_M = 1.5
    MASS_KG = 1.0
    set_workpiece(current_stage(), height=HEIGHT_M, mass=MASS_KG)


main()
