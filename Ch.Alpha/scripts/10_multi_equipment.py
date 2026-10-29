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
    EQUIPMENT_IDS = ("E01", "E02", "E03")
    STATE_COLORS = {"UNKNOWN": (0.45, 0.45, 0.45), "STALE": (0.3, 0.4, 0.55)}
    TARGET = "/World/Workpiece"
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
    def read_multi(path, max_age_s=3):
        if not math.isfinite(max_age_s) or max_age_s < 0:
            raise ValueError("max_age_s >= 0 이어야 합니다.")
        groups, seen = {}, set()
        with Path(path).open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                now, sample = float(row["time_s"]), float(row["sample_time_s"])
                key = row["equipment_id"]
                if key not in EQUIPMENT_IDS or not math.isfinite(now) or not math.isfinite(sample) or not 0 <= sample <= now:
                    raise ValueError("장비 ID 또는 시각이 올바르지 않습니다.")
                if (now,key) in seen:
                    raise ValueError("동일 시각과 장비의 중복 행입니다.")
                seen.add((now,key))
                temp = float(row["temperature_c"]) if row["temperature_c"].strip() else None
                vib = float(row["vibration_mm_s"]) if row["vibration_mm_s"].strip() else None
                if temp is not None and not math.isfinite(temp):
                    raise ValueError("온도는 유한한 수여야 합니다.")
                if vib is not None and (not math.isfinite(vib) or vib<0):
                    raise ValueError("진동은 유한한 0 이상 수여야 합니다.")
                if temp is None or vib is None:
                    state,color = "UNKNOWN",STATE_COLORS["UNKNOWN"]
                elif now-sample > max_age_s:
                    state,color = "STALE",STATE_COLORS["STALE"]
                else:
                    state,color = classify(temp,vib)
                groups.setdefault(now,[]).append(dict(time_s=now, equipment_id=key, temperature_c=temp,
                    vibration_mm_s=vib, sample_time_s=sample, state=state, color=color))
        if not groups:
            raise ValueError("CSV가 비어 있습니다.")
        for now, rows in groups.items():
            if {r["equipment_id"] for r in rows} != set(EQUIPMENT_IDS):
                raise ValueError(f"{now}초에 E01/E02/E03 행이 모두 필요합니다. 결측은 빈 값으로 표시하세요.")
        return [(now, sorted(rows,key=lambda r:r["equipment_id"])) for now,rows in sorted(groups.items())]

    def apply_multi(stage, rows):
        for row in rows:
            p = stage.GetPrimAtPath(f"/World/Stations/{row['equipment_id']}")
            if not p:
                raise ValueError("08_multi_equipment.usda를 먼저 여세요.")
            lamp = UsdGeom.Sphere(stage.GetPrimAtPath(str(p.GetPath())+"/Lamp"))
            lamp.CreateDisplayColorAttr(Vt.Vec3fArray([Gf.Vec3f(*row["color"])]))
            for key in ("state","equipment_id"):
                p.CreateAttribute("training:"+key,Sdf.ValueTypeNames.String).Set(row[key])
            p.CreateAttribute("training:source",Sdf.ValueTypeNames.String).Set("SYNTHETIC_MULTI_CSV")
            for key in ("time_s","sample_time_s","temperature_c","vibration_mm_s"):
                attr=p.CreateAttribute("training:"+key,Sdf.ValueTypeNames.Double)
                if row[key] is None:
                    attr.Block()  # 이전 수치가 정상 데이터처럼 남지 않도록 한다.
                else:
                    attr.Set(row[key])

    import asyncio

    async def replay_multi():
        s=omni.usd.get_context().get_stage()
        assert s.GetPrimAtPath("/World/Stations/E01"), "08_multi_equipment.usda를 여세요."
        assert omni.timeline.get_timeline_interface().is_stopped(), "Stop 후 실행하세요."
        history=[]
        previous=0
        for now,rows in read_multi(ROOT/"shared/data/multi_equipment.csv"):
            await asyncio.sleep(now-previous)
            if omni.usd.get_context().get_stage()!=s:
                raise RuntimeError("장면이 바뀌어 재생을 중지했습니다.")
            apply_multi(s,rows)
            for row in rows:
                item={k:row[k] for k in ("time_s","equipment_id","temperature_c","vibration_mm_s","state")}
                history.append(item)
                print(item)
            previous=now
        out=ROOT/"outputs/multi_equipment_report.csv"
        out.parent.mkdir(exist_ok=True)
        with out.open("w",encoding="utf-8-sig",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=list(history[0]))
            writer.writeheader()
            writer.writerows(history)
        save_result(s,"multi_equipment_final.usda")
        print(out)

    if any(t.get_name().startswith("alpha_workshop_") and not t.done() for t in asyncio.all_tasks()):
        print("교육 작업 실행 중입니다. 06_stop_tasks.py로 중단 후 실행하세요.")
    else:
        asyncio.get_running_loop().create_task(replay_multi(), name="alpha_workshop_10")


main()
