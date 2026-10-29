# Day 2 Part 2 · CAD Import 및 USD Hierarchy 정리

배정 60분: 설명 30분, 실습 30분. 입력: `02_structured.usda`, CAD 자료.

## 목표와 개념

Day 1의 변환 결과를 재사용하면서 편집 가능한 래퍼 Prim과 원본 내부 계층을 구분합니다. 자산 Reference 안의 이름을 무리하게 바꾸면 관계 경로가 깨질 수 있으므로 바깥 구조로 역할을 표현합니다.

## 따라하기

1. Day 1 변환 결과가 있으면 별도 장면에서 엽니다. 없으면 제공 USD를 확인합니다.
2. 공통 체크포인트 02로 돌아옵니다. Equipment는 CAD를 Reference하고 Workpiece는 독립 Cube임을 확인합니다.
3. 래퍼 Equipment의 Translate X=-1.5와 CAD 내부 변환을 비교합니다.
4. Equipment의 Translate를 약간 바꾸고 하위 형상이 함께 이동하는지 확인한 후 Undo합니다.
5. 선택 실습: 새 Xform `/World/CADComparison`을 만들고 제공 USD를 Reference로 연결합니다. 대상 Prim은 `/World`를 지정하거나 원본 defaultPrim을 사용합니다. X=2m로 이동하여 원래 장비와 비교하고 해당 래퍼를 삭제합니다.
6. CAD 원본의 내부 Prim을 이름 변경하거나 이동하지 않고 공통 장면으로 복귀합니다.

## 완료 확인

제출: `/World` 아래 역할별 계층도와 Equipment의 Reference 파일 경로. CAD를 구조화해도 정적 장비와 동적 작업물을 분리할 수 있어야 합니다.

변환기가 만든 계층이 제공 USD와 다르면 이후 코드의 Workpiece 경로는 유지하세요. 공통 장면을 통째로 새 CAD로 교체할 필요는 없습니다.

## 확장 실습

[추가 예제·오류 찾기·선택 과제](EXPANDED_LAB.md): 원본 물리와 override 확인. 기존 실습 시간 안에서 선택하여 진행합니다.
