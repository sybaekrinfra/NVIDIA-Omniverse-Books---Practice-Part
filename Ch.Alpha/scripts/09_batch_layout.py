import omni.usd,omni.timeline
from workshop_plus import batch_parts
assert omni.timeline.get_timeline_interface().is_stopped(), "Stop 후 실행하세요."
s=omni.usd.get_context().get_stage()
assert s.GetPrimAtPath("/World/Batch"), "07_batch_layout.usda를 여세요."
ROWS=2
COLUMNS=3
SPACING_M=0.45
paths=batch_parts(s,ROWS,COLUMNS,SPACING_M)
print("작업물 수:",len(paths))
print("\n".join(paths))
