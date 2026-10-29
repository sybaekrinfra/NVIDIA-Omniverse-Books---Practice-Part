"""강사용: 외부 자산 없는 1축 회전팔 체크포인트 생성. Isaac Sim Python 사용."""
from pathlib import Path
from pxr import Usd, UsdGeom, UsdPhysics, UsdLux, Gf

ROOT = Path(__file__).resolve().parents[1]

def build():
    stage = Usd.Stage.CreateInMemory()
    world = UsdGeom.Xform.Define(stage, '/World')
    stage.SetDefaultPrim(world.GetPrim())
    UsdGeom.SetStageMetersPerUnit(stage, 1)
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    scene = UsdPhysics.Scene.Define(stage, '/World/PhysicsScene')
    scene.CreateGravityDirectionAttr(Gf.Vec3f(0, 0, -1))
    scene.CreateGravityMagnitudeAttr(9.81)
    UsdLux.DomeLight.Define(stage, '/World/Light').CreateIntensityAttr(800)
    base = UsdGeom.Cube.Define(stage, '/World/Base')
    base.CreateSizeAttr(1)
    UsdGeom.XformCommonAPI(base).SetTranslate(Gf.Vec3d(0, 0, 0.5))
    UsdGeom.XformCommonAPI(base).SetScale(Gf.Vec3f(.2, .2, 1))
    base.CreateDisplayColorAttr([Gf.Vec3f(.35, .35, .4)])
    arm = UsdGeom.Xform.Define(stage, '/World/Arm')
    UsdGeom.XformCommonAPI(arm).SetTranslate(Gf.Vec3d(.5, 0, 1))
    mesh = UsdGeom.Cube.Define(stage, '/World/Arm/Shape')
    mesh.CreateSizeAttr(1)
    UsdGeom.XformCommonAPI(mesh).SetScale(Gf.Vec3f(1, .12, .12))
    mesh.CreateDisplayColorAttr([Gf.Vec3f(.1, .55, .9)])
    UsdPhysics.CollisionAPI.Apply(mesh.GetPrim())
    UsdPhysics.RigidBodyAPI.Apply(arm.GetPrim())
    UsdPhysics.MassAPI.Apply(arm.GetPrim()).CreateMassAttr(1)
    joint = UsdPhysics.RevoluteJoint.Define(stage, '/World/Hinge')
    joint.CreateBody1Rel().SetTargets(['/World/Arm'])
    joint.CreateLocalPos0Attr(Gf.Vec3f(0, 0, 1))  # body0 omitted: fixed world
    joint.CreateLocalPos1Attr(Gf.Vec3f(-.5, 0, 0))
    joint.CreateAxisAttr('Z')
    joint.CreateLowerLimitAttr(-60)
    joint.CreateUpperLimitAttr(60)
    UsdPhysics.ArticulationRootAPI.Apply(joint.GetPrim())
    drive = UsdPhysics.DriveAPI.Apply(joint.GetPrim(), 'angular')
    drive.CreateTypeAttr('force')
    drive.CreateTargetPositionAttr(0)
    drive.CreateStiffnessAttr(100)
    drive.CreateDampingAttr(10)
    drive.CreateMaxForceAttr(100)
    (ROOT/'checkpoints/12_joint_drive.usda').write_text(stage.GetRootLayer().ExportToString(), encoding='utf-8')

if __name__ == '__main__':
    build()
