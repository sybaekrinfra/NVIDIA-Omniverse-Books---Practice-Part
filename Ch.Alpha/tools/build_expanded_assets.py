"""확장 장면 생성. 준비된 기본 체크포인트를 참조하며 원본 CAD는 수정하지 않는다."""
from pathlib import Path
import sys
from pxr import Usd,UsdGeom,UsdPhysics,Gf,Vt,Sdf
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"shared/python"))
from workshop_plus import cube,batch_parts,apply_thermal,read_multi,apply_multi

def layer(name,base="02_structured.usda"):
    p=ROOT/"checkpoints"/name
    p.write_text('#usda 1.0\n(\n defaultPrim = "World"\n metersPerUnit = 1\n upAxis = "Z"\n subLayers = [@'+base+'@]\n)\n',encoding="utf-8")
    return Usd.Stage.Open(str(p)),p

def save(stage,path):
    path.write_text(stage.GetRootLayer().ExportToString(),encoding="utf-8")

def main():
    s,p=layer("05_layout_variants.usda")
    vs=s.GetPrimAtPath("/World").GetVariantSets().AddVariantSet("layout")
    for name,gap in [("compact",0.45),("wide",0.85)]:
        vs.AddVariant(name)
        vs.SetVariantSelection(name)
        with vs.GetVariantEditContext():
            for i in range(3):
                cube(s,f"/World/Trays/Tray_{i+1}",(0.4+i*gap,-1.1,0.06),(0.35,0.6,0.12),(0.45,0.5,0.55))
    vs.SetVariantSelection("compact")
    save(s,p)

    s,p=layer("06_physics_comparison.usda","03_physics.usda")
    s.GetPrimAtPath("/World/Workpiece").SetActive(False)
    for name,pos,mass in [("A",(0.5,0,1.5),1),("B",(1.1,0,1.5),5),("C",(1.7,0,2.5),1)]:
        obj=cube(s,"/World/Experiment/"+name,pos,(0.2,0.2,0.2),(0.15+mass*0.1,0.5,0.75))
        UsdPhysics.CollisionAPI.Apply(obj)
        UsdPhysics.RigidBodyAPI.Apply(obj)
        UsdPhysics.MassAPI.Apply(obj).CreateMassAttr(mass)
    save(s,p)

    s,p=layer("07_batch_layout.usda")
    batch_parts(s)
    save(s,p)

    s,p=layer("08_multi_equipment.usda")
    for i,key in enumerate(("E01","E02","E03")):
        x=0.3+i*1.0
        root=f"/World/Stations/{key}"
        obj=UsdGeom.Xform.Define(s,root).GetPrim()
        cube(s,root+"/Housing",(x,-1.5,0.4),(0.7,0.55,0.8),(0.65,0.68,0.7))
        lamp=UsdGeom.Sphere.Define(s,root+"/Lamp")
        lamp.CreateRadiusAttr(0.1)
        lamp.AddTranslateOp().Set(Gf.Vec3d(x,-1.5,1.0))
        lamp.CreateDisplayColorAttr(Vt.Vec3fArray([Gf.Vec3f(.45)]))
    apply_multi(s,read_multi(ROOT/"shared/data/multi_equipment.csv")[0][1])
    save(s,p)

    s,p=layer("09_thermal_field.usda")
    mesh=UsdGeom.Mesh.Define(s,"/World/ThermalPlate")
    points=[]
    for j in range(5):
        for i in range(7):
            points.append(Gf.Vec3f(i*.35-0.3,j*.35-2.4,0.3))
    indices=[]
    for j in range(4):
        for i in range(6):
            a=j*7+i
            indices.extend([a,a+1,a+8,a+7])
    mesh.CreatePointsAttr(points)
    mesh.CreateFaceVertexCountsAttr([4]*24)
    mesh.CreateFaceVertexIndicesAttr(indices)
    mesh.CreateSubdivisionSchemeAttr("none")
    mesh.CreateDoubleSidedAttr(True)
    apply_thermal(s,ROOT/"shared/data/thermal_baseline.csv")
    save(s,p)

    s,p=layer("10_fault_units.usda","03_physics.usda")
    UsdGeom.XformCommonAPI(s.GetPrimAtPath("/World/Equipment")).SetScale(Gf.Vec3f(.001))
    save(s,p)
    s,p=layer("11_fault_collision.usda","03_physics.usda")
    UsdPhysics.CollisionAPI(s.GetPrimAtPath("/World/Ground")).CreateCollisionEnabledAttr(False)
    save(s,p)
    print("확장 체크포인트 7개 생성 완료")

if __name__=="__main__":
    main()
