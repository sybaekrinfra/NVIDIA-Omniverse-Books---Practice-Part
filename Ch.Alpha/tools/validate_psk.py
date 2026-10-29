"""PSK 추가 장면·배포 링크 검사. GUI/PhysX 실행 검사는 별도."""
from pathlib import Path
import re
from pxr import Usd, UsdGeom, UsdPhysics, UsdUtils, Gf

ROOT = Path(__file__).resolve().parents[1]

def main():
    path = ROOT / 'checkpoints/12_joint_drive.usda'
    stage = Usd.Stage.Open(str(path))
    assert not UsdUtils.ComputeAllDependencies(str(path))[2]
    assert UsdGeom.GetStageMetersPerUnit(stage) == 1
    assert UsdGeom.GetStageUpAxis(stage) == 'Z'
    joint = UsdPhysics.RevoluteJoint.Get(stage, '/World/Hinge')
    assert joint.GetBody0Rel().GetTargets() == []
    assert [str(p) for p in joint.GetBody1Rel().GetTargets()] == ['/World/Arm']
    assert joint.GetAxisAttr().Get() == 'Z'
    assert joint.GetLowerLimitAttr().Get() == -60
    assert joint.GetUpperLimitAttr().Get() == 60
    assert joint.GetPrim().HasAPI(UsdPhysics.ArticulationRootAPI)
    arm = stage.GetPrimAtPath('/World/Arm')
    assert arm.HasAPI(UsdPhysics.RigidBodyAPI)
    assert UsdPhysics.MassAPI(arm).GetMassAttr().Get() == 1
    assert stage.GetPrimAtPath('/World/Arm/Shape').HasAPI(UsdPhysics.CollisionAPI)
    # Initial joint frames must coincide in world space.
    world_anchor = joint.GetLocalPos0Attr().Get()
    transform = UsdGeom.XformCache().GetLocalToWorldTransform(arm)
    arm_anchor = transform.Transform(joint.GetLocalPos1Attr().Get())
    assert (Gf.Vec3d(world_anchor) - arm_anchor).GetLength() < 1e-6
    drive = UsdPhysics.DriveAPI(joint, 'angular')
    assert drive.GetStiffnessAttr().Get() > 0
    assert drive.GetDampingAttr().Get() > 0
    assert drive.GetMaxForceAttr().Get() > 0
    stage.SetEditTarget(stage.GetSessionLayer())
    for value in (-45, 0, 30, 45):
        assert drive.GetTargetPositionAttr().Set(value)
        assert drive.GetTargetPositionAttr().Get() == value
    missing = []
    for doc in ROOT.rglob('*.md'):
        for link in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#'):
                continue
            target = link.split('#')[0]
            if target and not (doc.parent / target).exists():
                missing.append((str(doc.relative_to(ROOT)), link))
    assert not missing, missing
    assert not (ROOT / '.git').exists()
    print('PASS: joint schemas, world/body anchors, limits, drive targets, Markdown file links, no nested Git')
    print('NOT TESTED: GUI, PhysX joint motion, ROS 2, Replicator rendering')

if __name__ == '__main__':
    main()
