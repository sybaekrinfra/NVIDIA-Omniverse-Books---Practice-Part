import omni.timeline
from cbnu_lab import current_stage, add_physics
assert omni.timeline.get_timeline_interface().is_stopped(), "Stop 버튼을 누르세요."
add_physics(current_stage())
