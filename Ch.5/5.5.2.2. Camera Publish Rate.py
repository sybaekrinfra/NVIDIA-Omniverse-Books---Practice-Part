import isaacsim.core.experimental.utils.prim as prim_utils

camera_path = (
    "/World/BX200L/link6/camera_mount/camera_rgb"
)

camera_prim = prim_utils.get_prim_at_path(camera_path)
camera_prim.ApplyAPI("OmniSensorAPI")
camera_prim.GetAttribute("omni:sensor:tickRate").Set(30.0)

print("camera:", camera_path)
print("tick rate:", camera_prim.GetAttribute("omni:sensor:tickRate").Get())
