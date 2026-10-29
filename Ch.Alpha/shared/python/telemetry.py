"""가상 교육 데이터 판정. 실제 장비의 안전 임계값이 아니다."""
import csv
import math

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
