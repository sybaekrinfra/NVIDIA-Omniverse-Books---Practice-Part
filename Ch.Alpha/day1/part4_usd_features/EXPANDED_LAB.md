# D1P4 확장 실습 · 합성 결과와 배치 Variant

이 실습은 기존 Part 시간 안에서 선택해 진행합니다. 기존 기본 실습을 24분, 확장 활동을 14분으로 배분합니다. 도전 과제는 조기 완료자 또는 교육 후 복습용입니다. 확장 활동을 기존 실습 뒤에 모두 추가하지 않습니다.

## 상황과 목표

**compact와 wide 배치 검토**을 수행합니다. 시작 파일은 `checkpoints/05_layout_variants.usda`입니다. Python 예제는 Script Editor에서 `00_start_here.py`를 먼저 실행합니다. 원본 체크포인트는 저장하지 않고 결과를 outputs에 보관합니다.

## 가이드 실습

1. 기존 review/assembly 예제로 원본과 색 override를 확인한다.
2. 05를 열고 00_start_here.py를 실행한다.
3. 07_layout_variant.py에서 compact와 wide를 각각 선택한다.
4. Tray_1과 Tray_3의 X 차이를 비교한다. compact=0.9m, wide=1.7m이다.
5. 같은 자산을 복사하지 않고 배치 선택을 보관하는 이점을 적는다.

## 생각해 보기

Variant를 바꿨는데 위치가 그대로라면 무엇을 확인할까?

답을 보기 전에 팀원과 예상 결과를 적습니다. [강사용 해설](../../instructor/EXPANDED_ANSWERS.md#d1p4)에서 비교할 수 있습니다.

## 자주 발생하는 문제

증상: 잘못된 Stage에서 layout Variant 실행

복구: 05 체크포인트를 열고 Variant 이름을 출력한다.

## 선택 도전

기존 legacy_liverps/04_variant.usda에서 색 Variant를 확인하고 배치 Variant와 비교한다.

## 제출 및 통과 기준

두 배치 화면과 좌표 비교를 제출합니다. 결과만 보여주지 않고 설정 또는 데이터가 결과에 영향을 준 이유를 한 문장으로 설명하면 완료합니다.
