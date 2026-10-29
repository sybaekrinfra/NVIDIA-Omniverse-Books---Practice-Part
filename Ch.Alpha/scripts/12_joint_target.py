"""선택 실습: 회전 목표값 한 개만 변경. 00 초기화 불필요."""
import omni.usd
import omni.timeline
from pxr import UsdPhysics

TARGET_DEG = 30  # -45, 0, 30, 45 중 선택
assert omni.timeline.get_timeline_interface().is_stopped(), 'Stop 후 실행하세요.'
assert -60 <= TARGET_DEG <= 60, '관절 제한 -60~60도 안에서 지정하세요.'
stage = omni.usd.get_context().get_stage()
joint = stage.GetPrimAtPath('/World/Hinge') if stage else None
assert joint and joint.IsA(UsdPhysics.RevoluteJoint), '12_joint_drive.usda를 여세요.'
UsdPhysics.DriveAPI(joint, 'angular').GetTargetPositionAttr().Set(TARGET_DEG)
print('목표 각도:', TARGET_DEG, '도. Play하여 관찰하세요.')
