"""강사용: usd-core가 있는 별도 Python에서 배포용 체크포인트 재생성."""
from pathlib import Path
import sys
from pxr import Usd, UsdGeom, UsdLux, UsdPhysics, Gf, Vt, Sdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared/python"))
from cbnu_lab import add_physics, apply_sample, samples

def cube(stage, path, scale, pos, color):
    obj = UsdGeom.Cube.Define(stage, path)
    obj.CreateSizeAttr(1)
    obj.AddTranslateOp().Set(Gf.Vec3d(*pos))
    obj.AddScaleOp().Set(Gf.Vec3f(*scale))
    obj.CreateDisplayColorAttr(Vt.Vec3fArray([Gf.Vec3f(*color)]))
    return obj

def main():
    folder = ROOT / "checkpoints"
    folder.mkdir(exist_ok=True)
    stage = Usd.Stage.CreateNew(str(folder / "01_layout.usda"))
    world = UsdGeom.Xform.Define(stage, "/World")
    stage.SetDefaultPrim(world.GetPrim())
    UsdGeom.SetStageMetersPerUnit(stage, 1)
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    cube(stage, "/World/Ground", (8, 6, 0.1), (0, 0, -0.05), (0.22, 0.25, 0.3))
    cube(stage, "/World/Workpiece", (0.2, 0.2, 0.2), (1, 0, 1.5), (0.2, 0.5, 0.9))
    equipment = UsdGeom.Xform.Define(stage, "/World/Equipment")
    equipment.AddTranslateOp().Set(Gf.Vec3d(-1.5, 0, 0))
    equipment.GetPrim().GetReferences().AddReference("../shared/assets/cad/BX200L-C001.usd", "/World")
    # 기존 CAD 변환 USD에는 로봇 물리가 포함되어 있다. 원본은 보존하고
    # 수업 장면의 local override에서만 제거하여 작업물 낙하에 간섭하지 않게 한다.
    for prim in list(Usd.PrimRange(equipment.GetPrim())):
        if prim.IsA(UsdPhysics.Joint):
            prim.SetActive(False)
        for api in (UsdPhysics.ArticulationRootAPI, UsdPhysics.RigidBodyAPI,
                    UsdPhysics.CollisionAPI, UsdPhysics.MeshCollisionAPI):
            if prim.HasAPI(api):
                prim.RemoveAPI(api)
    lamp = UsdGeom.Sphere.Define(stage, "/World/StatusLamp")
    lamp.CreateRadiusAttr(0.15)
    lamp.AddTranslateOp().Set(Gf.Vec3d(0, 0, 2.5))
    lamp.CreateDisplayColorAttr(Vt.Vec3fArray([Gf.Vec3f(0.05, 0.8, 0.2)]))
    UsdLux.DomeLight.Define(stage, "/World/Light").CreateIntensityAttr(800)
    camera = UsdGeom.Camera.Define(stage, "/World/Camera")
    view = Gf.Matrix4d(1).SetLookAt(Gf.Vec3d(6, -9, 6), Gf.Vec3d(0, 0.5, 1), Gf.Vec3d(0, 0, 1))
    camera.AddTransformOp().Set(view.GetInverse())
    camera.CreateClippingRangeAttr(Gf.Vec2f(0.1, 1000))
    stage.GetRootLayer().Save()

    # 동일 디렉터리 안의 단계별 subLayer: 학습자의 편집과 복구를 분리한다.
    def layer(name, source):
        s = Usd.Stage.CreateNew(str(folder / name))
        s.GetRootLayer().subLayerPaths = [source]
        s.SetDefaultPrim(s.GetPrimAtPath("/World"))
        UsdGeom.SetStageMetersPerUnit(s, 1)
        UsdGeom.SetStageUpAxis(s, "Z")
        return s
    s = layer("02_structured.usda", "01_layout.usda")
    s.GetRootLayer().Save()
    s = layer("03_physics.usda", "02_structured.usda")
    add_physics(s)
    s.GetRootLayer().Save()
    s = layer("04_status.usda", "03_physics.usda")
    apply_sample(s, samples()[4])
    s.GetRootLayer().Save()

    # reference / payload / local override를 같은 단순 자산으로 비교한다.
    usd = ROOT / "shared/assets/usd_basics"
    usd.mkdir(parents=True, exist_ok=True)
    s = Usd.Stage.CreateNew(str(usd / "part.usda"))
    c = cube(s, "/Part", (1, 1, 1), (0, 0, 0), (0, 0.7, 0.9))
    s.SetDefaultPrim(c.GetPrim())
    s.GetRootLayer().Save()
    s = Usd.Stage.CreateNew(str(usd / "assembly.usda"))
    w = UsdGeom.Xform.Define(s, "/World").GetPrim()
    s.SetDefaultPrim(w)
    UsdGeom.SetStageMetersPerUnit(s, 1)
    UsdGeom.SetStageUpAxis(s, "Z")
    a = s.DefinePrim("/World/ReferencePart")
    a.GetReferences().AddReference("part.usda")
    a.GetAttribute("xformOp:translate").Set(Gf.Vec3d(-1, 0, 0))
    b = s.DefinePrim("/World/PayloadPart")
    b.GetPayloads().AddPayload("part.usda")
    b.GetAttribute("xformOp:translate").Set(Gf.Vec3d(1, 0, 0))
    s.GetRootLayer().Save()
    s = Usd.Stage.CreateNew(str(usd / "review.usda"))
    s.GetRootLayer().subLayerPaths = ["assembly.usda"]
    s.SetDefaultPrim(s.GetPrimAtPath("/World"))
    s.GetPrimAtPath("/World/ReferencePart").GetAttribute("primvars:displayColor").Set(Vt.Vec3fArray([Gf.Vec3f(1, 0.2, 0.1)]))
    s.GetRootLayer().Save()
    print("체크포인트 생성 완료")

if __name__ == "__main__":
    main()
