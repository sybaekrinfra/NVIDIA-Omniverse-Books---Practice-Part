"""Kit에서만 실행. UI를 막지 않고 시뮬레이션 시간 2초씩 두 실험 수행."""
import asyncio
import csv
import time
import omni.kit.app
import omni.timeline
import omni.usd
from cbnu_lab import ROOT, current_stage, set_workpiece, add_physics

async def run_experiments():
    stage = current_stage()
    timeline = omni.timeline.get_timeline_interface()
    app = omni.kit.app.get_app()
    timeline.stop()
    await app.next_update_async()
    add_physics(stage)
    rows = []
    try:
        for mass in (1.0, 5.0):
            timeline.stop()
            await app.next_update_async()
            set_workpiece(stage, height=1.5, mass=mass)
            timeline.set_current_time(0.0)
            timeline.play()
            wall_start = time.monotonic()
            while timeline.get_current_time() < 2.0:
                await app.next_update_async()
                if omni.usd.get_context().get_stage() != stage:
                    raise RuntimeError("장면이 변경되어 실험을 중단했습니다.")
                if not timeline.is_playing():
                    raise RuntimeError("사용자가 재생을 중단했습니다.")
                if time.monotonic() - wall_start > 60:
                    raise TimeoutError("60초 동안 시뮬레이션 시간 2초에 도달하지 못했습니다.")
            timeline.pause()
            rows.append({"mass_kg": mass, "height_m": 1.5,
                         "simulation_time_s": round(timeline.get_current_time(), 4),
                         "observation": "학습자가 Viewport 관찰 결과를 입력"})
            await asyncio.sleep(1)
    finally:
        timeline.stop()
    out = ROOT / "outputs/simulation_runs.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print("실행 조건 기록:", out, "(위치 측정 로그는 아님)")

if "cbnu_sim_task" in globals() and not cbnu_sim_task.done():
    print("이미 실행 중입니다. 완료 후 다시 실행하세요.")
else:
    cbnu_sim_task = asyncio.ensure_future(run_experiments())
