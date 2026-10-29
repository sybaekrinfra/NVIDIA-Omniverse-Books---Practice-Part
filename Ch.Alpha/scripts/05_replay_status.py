"""가상 CSV의 time_s 간격에 맞춰 상태 표시. 물리 Timeline과 독립적."""
import asyncio
import omni.usd
import omni.timeline
from cbnu_lab import current_stage, samples, apply_sample, save_result

async def replay():
    stage = current_stage()
    if not omni.timeline.get_timeline_interface().is_stopped():
        raise RuntimeError("물리 실험을 Stop한 후 실행하세요.")
    previous = 0.0
    for sample in samples():
        await asyncio.sleep(sample[0] - previous)
        if omni.usd.get_context().get_stage() != stage:
            raise RuntimeError("장면이 변경되어 재생을 중단했습니다.")
        apply_sample(stage, sample)
        previous = sample[0]
    save_result(stage, "day2_final.usda")

if "cbnu_status_task" in globals() and not cbnu_status_task.done():
    print("상태 재생 중입니다. 완료 후 다시 실행하세요.")
else:
    cbnu_status_task = asyncio.ensure_future(replay())
