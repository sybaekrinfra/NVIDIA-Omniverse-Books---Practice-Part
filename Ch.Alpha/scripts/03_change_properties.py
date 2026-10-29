import omni.timeline
from cbnu_lab import current_stage, set_workpiece
assert omni.timeline.get_timeline_interface().is_stopped(), "Stop 버튼을 누르세요."

# 학습자 변경 지점: 먼저 높이만 바꾸고 다음에 질량을 바꾸세요.
HEIGHT_M = 1.5
MASS_KG = 1.0
set_workpiece(current_stage(), height=HEIGHT_M, mass=MASS_KG)
