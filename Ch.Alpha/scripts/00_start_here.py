"""선택 실행: 현재 열린 장면 확인. 다른 스크립트 실행의 전제 조건이 아닙니다."""
import omni.usd

stage = omni.usd.get_context().get_stage()
if stage is None:
    print("먼저 checkpoints의 실습 장면을 여세요.")
else:
    print("열린 장면:", stage.GetRootLayer().identifier)
    print("각 scripts 파일을 독립 실행할 수 있습니다. 00 실행은 선택입니다.")
