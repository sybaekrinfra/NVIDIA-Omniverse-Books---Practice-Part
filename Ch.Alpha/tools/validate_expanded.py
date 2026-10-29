"""확장 실습의 데이터·합성·진단 검사. PhysX/Kit UI 실행 검증과 구별한다."""
from pathlib import Path
import sys,ast,tempfile,math
from pxr import Usd,Sdf,UsdGeom,UsdPhysics
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'shared/python'))
from workshop_plus import readiness,batch_parts,read_multi,apply_multi,apply_thermal,thermal_colors

def memory_scene(name):
    original=Usd.Stage.Open(str(ROOT/'checkpoints'/name))
    return Usd.Stage.Open(original.Flatten())

def main():
    for f in ROOT.rglob('*.py'):
        ast.parse(f.read_text(encoding='utf-8'),filename=str(f))
    s=Usd.Stage.Open(str(ROOT/'checkpoints/05_layout_variants.usda'))
    s.SetEditTarget(s.GetSessionLayer())
    v=s.GetPrimAtPath('/World').GetVariantSets().GetVariantSet('layout')
    for name,distance in [('compact',.9),('wide',1.7)]:
        assert v.SetVariantSelection(name)
        a=s.GetPrimAtPath('/World/Trays/Tray_1').GetAttribute('xformOp:translate').Get()[0]
        b=s.GetPrimAtPath('/World/Trays/Tray_3').GetAttribute('xformOp:translate').Get()[0]
        assert abs(b-a-distance)<1e-6
    assert all(ok for _,ok in readiness(memory_scene('03_physics.usda')))
    for file,check in [('10_fault_units.usda','equipment_height_1_to_3m'),('11_fault_collision.usda','ground_collider')]:
        s=memory_scene(file)
        results=dict(readiness(s))
        assert not results[check],results
        if 'units' in file:
            UsdGeom.XformCommonAPI(s.GetPrimAtPath('/World/Equipment')).SetScale((1,1,1))
        else:
            UsdPhysics.CollisionAPI(s.GetPrimAtPath('/World/Ground')).CreateCollisionEnabledAttr(True)
        assert all(ok for _,ok in readiness(s))
    s=memory_scene('07_batch_layout.usda')
    for r,c in [(2,3),(3,4),(1,1),(2,3)]:
        paths=batch_parts(s,r,c)
        assert len(paths)==r*c
        assert len(list(s.GetPrimAtPath('/World/Batch').GetChildren()))==r*c
        assert len(set(paths))==r*c
    groups=read_multi(ROOT/'shared/data/multi_equipment.csv')
    assert len(groups)==4 and sum(len(rows) for _,rows in groups)==12
    assert groups[1][1][2]['state']=='UNKNOWN'
    assert [x['state'] for x in groups[-1][1]]==['NORMAL','STALE','ALARM']
    s=memory_scene('08_multi_equipment.usda')
    for _,rows in groups:
        apply_multi(s,rows)
        if rows[2]['state']=='UNKNOWN':
            assert s.GetPrimAtPath('/World/Stations/E03').GetAttribute('training:temperature_c').Get() is None
    with tempfile.TemporaryDirectory() as folder:
        f=Path(folder)/'test.csv'
        header='time_s,sample_time_s,equipment_id,temperature_c,vibration_mm_s\n'
        f.write_text(header+'3,0,E01,40,1\n3,0,E02,40,1\n3,0,E03,40,1\n',encoding='utf-8')
        assert all(x['state']=='NORMAL' for x in read_multi(f)[0][1])
        for rows in ['0,0,E01,40,1\n','0,0,E01,40,1\n0,0,E01,40,1\n']:
            f.write_text(header+rows,encoding='utf-8')
            try:read_multi(f)
            except ValueError:pass
            else:raise AssertionError('malformed input accepted')
    s=memory_scene('09_thermal_field.usda')
    for file,bounds in [('thermal_baseline.csv',(30,45)),('thermal_hotspot.csv',(30,95))]:
        assert apply_thermal(s,ROOT/'shared/data'/file)==bounds
        pv=UsdGeom.Mesh(s.GetPrimAtPath('/World/ThermalPlate')).GetDisplayColorPrimvar()
        assert pv.GetInterpolation()=='uniform' and len(pv.Get())==24
    for values,low,high in [([math.nan],20,100),([40],50,50)]:
        try:thermal_colors(values,low,high)
        except ValueError:pass
        else:raise AssertionError('bad range accepted')
    s=memory_scene('06_physics_comparison.usda')
    bodies=[x for x in s.Traverse() if x.HasAPI(UsdPhysics.RigidBodyAPI)]
    assert {str(x.GetPath()) for x in bodies}=={'/World/Experiment/A','/World/Experiment/B','/World/Experiment/C'}
    print('PASS: variants, 2 fault diagnostics and repair, 4 batch sizes, 12 telemetry records, missing/stale data, 2 thermal fields, 3 dynamic bodies')
    print('NOT TESTED: Isaac Sim GUI, PhysX runtime, Kit asyncio, CAD Converter, Nucleus')

if __name__=='__main__':main()
