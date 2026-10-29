"""Script Editor에서 이 파일 전체를 실행하세요. 초기화 스크립트가 필요 없습니다."""

def main():
    import math
    import omni.usd
    import omni.timeline
    from pxr import Usd, UsdGeom, UsdPhysics
    TARGET = "/World/Workpiece"

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

    s=omni.usd.get_context().get_stage()
    assert s, "실습 장면을 먼저 여세요."
    for name,passed in readiness(s):
        print("PASS" if passed else "CHECK",name)
    print("교육용 조건 점검이며 SimReady 인증 결과가 아닙니다.")


main()
