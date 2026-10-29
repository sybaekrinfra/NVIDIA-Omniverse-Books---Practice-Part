"""Script Editor에서 이 파일 전체를 실행하세요. 초기화 스크립트가 필요 없습니다."""

def main():
    from pathlib import Path
    import math
    import csv
    import omni.usd
    import omni.timeline
    from pxr import UsdGeom, UsdPhysics, Gf
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
    TARGET = "/World/Workpiece"
    def current_stage():
        stage = omni.usd.get_context().get_stage()
        if not stage or not stage.GetPrimAtPath("/World/StatusLamp") or not stage.GetPrimAtPath(TARGET):
            raise RuntimeError("checkpoints 폴더의 교육 장면을 먼저 여세요.")
        return stage

    def add_physics(stage):
        """단순 Cube만 동적 강체로 설정. CAD 장비는 시각 참조용."""
        if UsdGeom.GetStageMetersPerUnit(stage) != 1 or UsdGeom.GetStageUpAxis(stage) != "Z":
            raise ValueError("본 실습은 meter / Z-up 기준입니다.")
        scene = UsdPhysics.Scene.Define(stage, "/World/PhysicsScene")
        scene.CreateGravityDirectionAttr(Gf.Vec3f(0, 0, -1))
        scene.CreateGravityMagnitudeAttr(9.81)
        floor = stage.GetPrimAtPath("/World/Ground")
        obj = stage.GetPrimAtPath(TARGET)
        if not floor or not obj:
            raise ValueError("Ground와 Workpiece가 필요합니다.")
        UsdPhysics.CollisionAPI.Apply(floor).CreateCollisionEnabledAttr(True)
        UsdPhysics.CollisionAPI.Apply(obj).CreateCollisionEnabledAttr(True)
        body = UsdPhysics.RigidBodyAPI.Apply(obj)
        body.CreateRigidBodyEnabledAttr(True)
        body.CreateKinematicEnabledAttr(False)
        UsdPhysics.MassAPI.Apply(obj).CreateMassAttr(1.0)
        print("Physics: gravity 9.81 m/s², Workpiece mass 1 kg")

    def set_workpiece(stage, height=1.5, mass=1.0):
        if not math.isfinite(height) or not math.isfinite(mass) or height < 0.1 or mass <= 0:
            raise ValueError("height >= 0.1 m, mass > 0 kg 조건을 지키세요.")
        p = stage.GetPrimAtPath(TARGET)
        # 준비된 단일 translate op만 변경하여 복잡한 CAD transform을 보존한다.
        position_attr = p.GetAttribute("xformOp:translate")
        position = position_attr.Get()
        if position is None:
            raise ValueError("Workpiece에 translate 속성이 필요합니다.")
        position_attr.Set(Gf.Vec3d(position[0], position[1], height))
        UsdPhysics.MassAPI.Apply(p).CreateMassAttr(mass)
        print("height(m)=", height, "mass(kg)=", mass)


    """Kit에서만 실행. UI를 막지 않고 시뮬레이션 시간 2초씩 두 실험 수행."""
    import asyncio
    import time
    import omni.kit.app

    async def run_experiments():
        stage = current_stage()
        timeline = omni.timeline.get_timeline_interface()
        app = omni.kit.app.get_app()
        timeline.stop()
        await app.next_update_async()
        if omni.usd.get_context().get_stage() != stage:
            raise RuntimeError("장면이 변경되어 실험을 중단했습니다.")
        add_physics(stage)
        rows = []
        original_end = timeline.get_end_time()
        original_looping = timeline.is_looping()
        timeline.set_end_time(max(original_end, 3.0))
        timeline.set_looping(False)
        try:
            for mass in (1.0, 5.0):
                timeline.stop()
                await app.next_update_async()
                if omni.usd.get_context().get_stage() != stage:
                    raise RuntimeError("장면이 변경되어 실험을 중단했습니다.")
                set_workpiece(stage, height=1.5, mass=mass)
                timeline.set_current_time(0.0)
                timeline.play()
                wall_start = time.monotonic()
                while timeline.get_current_time() < 2.0:
                    await app.next_update_async()
                    if omni.usd.get_context().get_stage() != stage:
                        raise RuntimeError("장면이 변경되어 실험을 중단했습니다.")
                    if not timeline.is_playing():
                        raise RuntimeError("사용자가 재생을 중단했습니다.")
                    if time.monotonic() - wall_start > 60:
                        raise TimeoutError("60초 동안 시뮬레이션 시간 2초에 도달하지 못했습니다.")
                timeline.pause()
                rows.append({"mass_kg": mass, "height_m": 1.5,
                             "simulation_time_s": round(timeline.get_current_time(), 4),
                             "observation": "학습자가 Viewport 관찰 결과를 입력"})
                await asyncio.sleep(1)
        finally:
            if omni.usd.get_context().get_stage() == stage:
                timeline.stop()
                timeline.set_end_time(original_end)
                timeline.set_looping(original_looping)
        out = ROOT / "outputs/simulation_runs.csv"
        out.parent.mkdir(exist_ok=True)
        with out.open("w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        print("실행 조건 기록:", out, "(위치 측정 로그는 아님)")

    if any(t.get_name().startswith("alpha_workshop_") and not t.done() for t in asyncio.all_tasks()):
        print("교육 작업 실행 중입니다. 06_stop_tasks.py로 중단 후 실행하세요.")
    else:
        asyncio.get_running_loop().create_task(run_experiments(), name="alpha_workshop_04")


main()
