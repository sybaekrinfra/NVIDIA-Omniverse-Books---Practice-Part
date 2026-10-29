"""현재 장면을 독립적으로 열 수 있는 Flatten USD로 저장합니다."""

def main():
    from pathlib import Path
    import omni.usd
    import omni.timeline
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

    # 실습별 제출 파일 이름만 변경하세요.
    FILE_NAME = "team01_result.usda"
    stage = omni.usd.get_context().get_stage()
    if stage is None:
        raise RuntimeError("저장할 장면을 먼저 여세요.")
    save_result(stage, FILE_NAME)


main()
