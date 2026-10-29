"""Script Editor에서 이 파일 전체를 실행하세요. 초기화 스크립트가 필요 없습니다."""

def main():
    import omni.usd
    import omni.timeline
    from pxr import UsdGeom, UsdPhysics, Gf
    TARGET = "/World/Workpiece"
    def current_stage():
        stage = omni.usd.get_context().get_stage()
        if not stage or not stage.GetPrimAtPath("/World/StatusLamp") or not stage.GetPrimAtPath(TARGET):
            raise RuntimeError("checkpoints 폴더의 교육 장면을 먼저 여세요.")
        return stage

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
        UsdPhysics.CollisionAPI.Apply(floor).CreateCollisionEnabledAttr(True)
        UsdPhysics.CollisionAPI.Apply(obj).CreateCollisionEnabledAttr(True)
        body = UsdPhysics.RigidBodyAPI.Apply(obj)
        body.CreateRigidBodyEnabledAttr(True)
        body.CreateKinematicEnabledAttr(False)
        UsdPhysics.MassAPI.Apply(obj).CreateMassAttr(1.0)
        print("Physics: gravity 9.81 m/s², Workpiece mass 1 kg")


    assert omni.timeline.get_timeline_interface().is_stopped(), "Stop 버튼을 누르세요."
    add_physics(current_stage())


main()
