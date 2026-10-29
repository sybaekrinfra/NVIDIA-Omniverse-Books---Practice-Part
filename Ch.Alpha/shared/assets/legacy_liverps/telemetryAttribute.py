import omni.usd
import asyncio, random, time
from pxr import Sdf

stage = omni.usd.get_context().get_stage()
pump = stage.GetPrimAtPath(
  "/World/Equipment/Pump"
)

async def simulate_sensor():
  for _ in range(15):
    temp = round(random.uniform(60.0, 85.0), 1)
    pump.CreateAttribute(
      "telemetry:temperatureC",
      Sdf.ValueTypeNames.Float
    ).Set(temp)
    await asyncio.sleep(1.0)

asyncio.ensure_future(simulate_sensor())
