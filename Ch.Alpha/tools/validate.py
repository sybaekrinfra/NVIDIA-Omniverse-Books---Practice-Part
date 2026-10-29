"""python tools/validate.py — usd-core가 있는 별도 Python. GUI/PhysX 검증 제외."""
from pathlib import Path
import ast
import math
import sys
from pxr import Usd, UsdGeom, UsdPhysics, UsdUtils

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared/python"))
from cbnu_lab import add_physics, set_workpiece, apply_sample
from telemetry import classify, read_samples

def main():
    for p in ROOT.rglob("*.py"):
        ast.parse(p.read_text(encoding="utf-8"), filename=str(p))
    files = list((ROOT / "checkpoints").glob("*.usda")) + list((ROOT / "shared/assets").rglob("*.usd*"))
    failures = []
    for p in files:
        try:
            s = Usd.Stage.Open(str(p))
            assert s
            _, _, missing = UsdUtils.ComputeAllDependencies(str(p))
            assert not missing, f"Unresolved: {missing}"
        except Exception as e:
            failures.append((str(p.relative_to(ROOT)), str(e)))
    if failures:
        raise AssertionError(failures)
    s = Usd.Stage.Open(str(ROOT / "checkpoints/03_physics.usda"))
    s.SetEditTarget(s.GetSessionLayer())
    assert UsdGeom.GetStageMetersPerUnit(s) == 1
    assert UsdGeom.GetStageUpAxis(s) == "Z"
    assert str(s.GetDefaultPrim().GetPath()) == "/World"
    p = s.GetPrimAtPath("/World/Workpiece")
    assert p.HasAPI(UsdPhysics.RigidBodyAPI) and p.HasAPI(UsdPhysics.CollisionAPI)
    assert s.GetPrimAtPath("/World/Ground").HasAPI(UsdPhysics.CollisionAPI)
    assert not s.GetPrimAtPath("/World/Ground").HasAPI(UsdPhysics.RigidBodyAPI)
    for prim in Usd.PrimRange(s.GetPrimAtPath("/World/Equipment")):
        assert not prim.HasAPI(UsdPhysics.RigidBodyAPI), prim.GetPath()
        assert not prim.HasAPI(UsdPhysics.ArticulationRootAPI), prim.GetPath()
        assert not prim.HasAPI(UsdPhysics.CollisionAPI), prim.GetPath()
        assert not prim.IsA(UsdPhysics.Joint), prim.GetPath()
    count = len(list(s.Traverse()))
    add_physics(s)
    add_physics(s)
    assert len(list(s.Traverse())) == count
    set_workpiece(s, height=2, mass=5)
    assert p.GetAttribute("physics:mass").Get() == 5
    assert p.GetAttribute("xformOp:translate").Get()[2] == 2
    rows = read_samples(ROOT / "shared/data/equipment_status.csv")
    assert [r[3] for r in rows] == ["NORMAL", "NORMAL", "WARNING", "WARNING", "ALARM", "ALARM", "NORMAL", "NORMAL"]
    for t,v,state in [(59.9,3.9,"NORMAL"),(60,0,"WARNING"),(79.9,0,"WARNING"),(80,0,"ALARM"),(0,4,"WARNING"),(0,6.9,"WARNING"),(0,7,"ALARM")]:
        assert classify(t,v)[0] == state
    for t,v in [(math.nan,0),(0,math.inf),(0,-1)]:
        try:
            classify(t,v)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid telemetry accepted")
    for row in rows:
        apply_sample(s,row)
        assert s.GetPrimAtPath("/World/Equipment").GetAttribute("training:state").Get() == row[3]
    flat = Usd.Stage.Open(s.Flatten())
    assert flat.GetPrimAtPath("/World/Equipment").GetAttribute("training:state").Get() == "NORMAL"
    b = Usd.Stage.Open(str(ROOT / "shared/assets/usd_basics/review.usda"))
    color = b.GetPrimAtPath("/World/ReferencePart").GetAttribute("primvars:displayColor").Get()[0]
    assert abs(color[0]-1) < 1e-5 and abs(color[1]-.2) < 1e-5
    b.Unload("/World/PayloadPart")
    assert not b.GetPrimAtPath("/World/PayloadPart").IsLoaded()
    b.Load("/World/PayloadPart")
    assert b.GetPrimAtPath("/World/PayloadPart").IsLoaded()
    print(f"PASS: {len(files)} USD files, references, schemas, idempotence, property edits, CSV boundaries, composition, flatten")
    print("NOT TESTED: Isaac Sim GUI, PhysX runtime, CAD conversion, Nucleus connection")

if __name__ == "__main__":
    main()
