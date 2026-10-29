# 진행 중인 교육용 비동기 작업만 중지한다.
for task_name in ("cbnu_sim_task", "cbnu_status_task", "cbnu_multi_task"):
    task = globals().get(task_name)
    if task and not task.done():
        task.cancel()
import omni.timeline
omni.timeline.get_timeline_interface().stop()
print("교육 작업 중지")
