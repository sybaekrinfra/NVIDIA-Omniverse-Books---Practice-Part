import asyncio,csv
import omni.usd,omni.timeline
from cbnu_lab import ROOT,save_result
from workshop_plus import read_multi,apply_multi

async def replay_multi():
    s=omni.usd.get_context().get_stage()
    assert s.GetPrimAtPath("/World/Stations/E01"), "08_multi_equipment.usda를 여세요."
    assert omni.timeline.get_timeline_interface().is_stopped(), "Stop 후 실행하세요."
    history=[]
    previous=0
    for now,rows in read_multi(ROOT/"shared/data/multi_equipment.csv"):
        await asyncio.sleep(now-previous)
        if omni.usd.get_context().get_stage()!=s:
            raise RuntimeError("장면이 바뀌어 재생을 중지했습니다.")
        apply_multi(s,rows)
        for row in rows:
            item={k:row[k] for k in ("time_s","equipment_id","temperature_c","vibration_mm_s","state")}
            history.append(item)
            print(item)
        previous=now
    out=ROOT/"outputs/multi_equipment_report.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w",encoding="utf-8-sig",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(history[0]))
        writer.writeheader()
        writer.writerows(history)
    save_result(s,"multi_equipment_final.usda")
    print(out)

if "cbnu_multi_task" in globals() and not cbnu_multi_task.done():
    print("이미 실행 중입니다.")
else:
    cbnu_multi_task=asyncio.ensure_future(replay_multi())
