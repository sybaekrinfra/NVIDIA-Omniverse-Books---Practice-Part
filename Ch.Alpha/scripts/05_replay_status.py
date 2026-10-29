"""Script Editor에서 이 파일 전체를 실행하세요. 초기화 스크립트가 필요 없습니다."""

def main():
    from pathlib import Path
    import math
    import csv
    import omni.usd
    import omni.timeline
    from pxr import UsdGeom, Sdf, Gf, Vt
    # CSV・저장 경로. 자동 탐색 실패 시에만 아래 값을 수정하세요.
    ROOT = None  # 예: Path(r"C:/omniverse/Ch.Alpha")
    if ROOT is None:
        opened_stage = omni.usd.get_context().get_stage()
        file_path = opened_stage.GetRootLayer().realPath if opened_stage else ""
        ROOT = next((p for p in Path(file_path).parents
                     if (p / "checkpoints").is_dir() and (p / "shared/data").is_dir()), None) if file_path else None
    if ROOT is None:
        raise RuntimeError("Ch.Alpha의 장면을 열거나 이 파일의 ROOT를 지정하세요.")
    ROOT = Path(ROOT).expanduser().resolve()
    if not (ROOT / "shared/data").is_dir():
        raise RuntimeError("ROOT는 shared/data를 포함한 Ch.Alpha 폴더여야 합니다.")
    def classify(temperature_c, vibration_mm_s):
        t, v = float(temperature_c), float(vibration_mm_s)
        if not math.isfinite(t) or not math.isfinite(v) or v < 0:
            raise ValueError("유한한 온도 및 0 이상의 진동 값이 필요합니다.")
        if t >= 80 or v >= 7:
            return "ALARM", (0.9, 0.05, 0.05)
        if t >= 60 or v >= 4:
            return "WARNING", (1.0, 0.65, 0.0)
        return "NORMAL", (0.05, 0.8, 0.2)
    def read_samples(path):
        with open(path, encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        if not rows:
            raise ValueError("CSV에 데이터가 없습니다.")
        result = []
        last = -1.0
        for row in rows:
            sec = float(row["time_s"])
            t = float(row["temperature_c"])
            v = float(row["vibration_mm_s"])
            if not math.isfinite(sec) or sec < 0 or sec <= last:
                raise ValueError("time_s는 0 이상이며 증가해야 합니다.")
            state, color = classify(t, v)
            result.append((sec, t, v, state, color))
            last = sec
        return result
    TARGET = "/World/Workpiece"
    def current_stage():
        stage = omni.usd.get_context().get_stage()
        if not stage or not stage.GetPrimAtPath("/World/StatusLamp") or not stage.GetPrimAtPath(TARGET):
            raise RuntimeError("checkpoints 폴더의 교육 장면을 먼저 여세요.")
        return stage

    def samples():
        return read_samples(ROOT / "shared/data/equipment_status.csv")

    def apply_sample(stage, sample):
        sec, t, v, state, color = sample
        lamp = UsdGeom.Sphere(stage.GetPrimAtPath("/World/StatusLamp"))
        lamp.CreateDisplayColorAttr(Vt.Vec3fArray([Gf.Vec3f(*color)]))
        p = stage.GetPrimAtPath("/World/Equipment")
        for name, typ, value in [
            ("training:time_s", Sdf.ValueTypeNames.Double, sec),
            ("training:temperature_c", Sdf.ValueTypeNames.Float, t),
            ("training:vibration_mm_s", Sdf.ValueTypeNames.Float, v),
            ("training:state", Sdf.ValueTypeNames.String, state),
            ("training:source", Sdf.ValueTypeNames.String, "SYNTHETIC_CSV"),
        ]:
            p.CreateAttribute(name, typ, custom=True).Set(value)
        print(f"{sec:4.1f}s {t:4.1f}°C {v:3.1f}mm/s {state}")

    def save_result(stage, name):
        if Path(name).name != name or not name.endswith(".usda"):
            raise ValueError("파일 이름만 지정하세요. 확장자는 .usda입니다.")
        dest = ROOT / "outputs" / name
        dest.parent.mkdir(exist_ok=True)
        # 상대 경로 유실을 방지하는 단일 파일 제출본. 원래 composition은 checkpoints에 보존.
        # Python 파일 쓰기로 Windows USD writer의 비ASCII 경로 문제를 피한다.
        dest.write_text(stage.Flatten().ExportToString(), encoding="utf-8")
        print("Saved flattened submission:", dest)
        return dest


    """가상 CSV의 time_s 간격에 맞춰 상태 표시. 물리 Timeline과 독립적."""
    import asyncio

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

    if any(t.get_name().startswith("alpha_workshop_") and not t.done() for t in asyncio.all_tasks()):
        print("교육 작업 실행 중입니다. 06_stop_tasks.py로 중단 후 실행하세요.")
    else:
        asyncio.get_running_loop().create_task(replay(), name="alpha_workshop_05")


main()
