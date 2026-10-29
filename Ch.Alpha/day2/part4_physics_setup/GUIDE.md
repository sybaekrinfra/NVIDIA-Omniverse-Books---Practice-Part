# Day 2 Part 4 · Collider, Rigid Body, Mass 설정

배정 45분: 설명 22분, 실습 23분. 입력: `02_structured.usda`, `scripts/02_apply_physics.py`.

## 따라하기

1. 02 체크포인트를 열고 Timeline을 Stop합니다. 강사는 바닥과 작업물 위치를 확인합니다.
2. GUI의 Add Physics 항목에서 Workpiece에 Collider, Rigid Body, Mass=1kg을 설정합니다. Ground에는 Collider만 설정합니다. PhysicsScene의 중력을 -Z, 9.81로 설정합니다.
3. GUI 메뉴가 다르거나 설정이 막히면 02 스크립트를 실행합니다. 스크립트는 같은 API를 적용하며 반복 실행해도 같은 경로를 사용합니다.
4. Play 후 작업물이 바닥에 멈추는지 관찰합니다. 중심 높이는 약 0.1m이며 접촉 여유·solver 설정으로 약간 다를 수 있습니다.
5. Stop합니다. Workpiece의 RigidBodyEnabled를 끄고 Play하여 차이를 확인합니다. 다시 Stop하고 02를 실행해 복원합니다.
6. 시간을 확보하면 Ground Collider를 일시 비활성화하여 바닥 통과를 관찰하고 원래 상태로 복구합니다.

## 완료 확인

제출: 작업물 Mass, Rigid Body, Collider 속성 화면과 낙하 후 화면. 바닥은 움직이지 않고 작업물만 낙하하면 통과합니다. 복구가 어려우면 03_physics를 엽니다.

CAD 장비에는 물리 API를 일괄 적용하지 않습니다. 시각 참조인 장비를 통과하는 현상은 이번 작업물-바닥 검증 범위 밖입니다.

## 확장 실습

[추가 예제·오류 찾기·선택 과제](EXPANDED_LAB.md): 누락된 충돌 설정 찾기. 기존 실습 시간 안에서 선택하여 진행합니다.
