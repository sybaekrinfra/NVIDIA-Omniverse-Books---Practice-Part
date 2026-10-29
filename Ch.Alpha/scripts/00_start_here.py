"""Isaac Sim Script Editor: 체크포인트를 먼저 연 뒤 실행하세요."""
from pathlib import Path
import sys
import omni.usd

# 자동 탐색에 실패할 때만 자신의 Ch.Alpha 절대 경로를 입력하세요.
ROOT = None  # 예: Path(r"C:/omniverse/NVIDIA-Omniverse-Books---Practice-Part/Ch.Alpha")
if ROOT is None:
    stage = omni.usd.get_context().get_stage()
    layer_path = stage.GetRootLayer().realPath if stage else ""
    if layer_path:
        ROOT = next((p for p in Path(layer_path).parents
                     if (p / "shared/python/cbnu_lab.py").is_file()), None)
if ROOT is None or not (Path(ROOT) / "shared/python/cbnu_lab.py").is_file():
    raise RuntimeError("Ch.Alpha/checkpoints 안의 장면을 먼저 여세요. 또는 ROOT를 지정하세요.")
ROOT = Path(ROOT).resolve()
loaded = sys.modules.get("cbnu_lab")
if loaded and Path(loaded.__file__).resolve().parents[2] != ROOT:
    raise RuntimeError("다른 워크숍 모듈이 로드되어 있습니다. 앱 재시작 후 다시 실행하세요.")
module_dir = str(ROOT / "shared/python")
if module_dir not in sys.path:
    sys.path.insert(0, module_dir)
import cbnu_lab
print("교육 자료:", cbnu_lab.ROOT)
print("준비 완료. 실습 가이드의 다음 스크립트를 실행하세요.")
