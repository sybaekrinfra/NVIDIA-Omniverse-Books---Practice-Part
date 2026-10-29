"""Script Editor 탭과 무관하게 교육용 비동기 작업 중단."""
import asyncio
import omni.timeline

for task in asyncio.all_tasks():
    if task.get_name().startswith("alpha_workshop_") and not task.done():
        task.cancel()
omni.timeline.get_timeline_interface().stop()
print("교육 작업 중단 요청 및 Timeline Stop")
