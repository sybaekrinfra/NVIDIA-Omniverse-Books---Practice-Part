# Day 1 Part 2 · Omniverse App UI 및 조작

배정 40분: 설명 20분, 가이드 실습 20분. 입력: `checkpoints/01_layout.usda`. 코드 없이 진행합니다.

## 목표와 개념

Viewport에서 보이는 대상과 Stage의 Prim 경로를 연결하고 Property에서 위치를 바꿉니다. Xform은 변환을 담는 구조이고 Cube는 보이는 형상입니다. 화면의 시점 이동과 물체의 위치 이동을 구별합니다.

## 따라하기

1. Stage에서 `/World/Workpiece`를 선택합니다. 선택 테두리와 Property의 Translate를 확인합니다.
2. Frame Selection으로 확대하고 orbit·pan·zoom을 연습합니다. 앱의 카메라 조작 도움말을 확인합니다.
3. Translate X를 1에서 1.5로 바꿉니다. 카메라만 이동했을 때와 비교합니다.
4. Undo로 복원하고 Z=1.5인지 확인합니다. Workpiece의 Size=1, Scale=(0.2,0.2,0.2)이므로 한 변은 0.2m입니다.
5. `/World/Equipment`를 펼쳐 CAD 하위 구조를 확인합니다. 장비의 내부 Prim 이름은 바꾸지 않습니다.
6. `/World/Camera`로 전체 화면을 확인합니다. 원본 저장 없이 다시 열어 초기 상태로 돌아옵니다.

## 완료 확인

작업물의 경로와 3축 위치를 기록합니다. 제출: 이동 전후 화면 2장 및 카메라 조작과 객체 변환의 차이 한 문장.

선택이 어렵다면 Viewport 대신 Stage에서 선택하세요. 전체 화면이 사라지면 `/World`를 Frame Selection합니다.

## 확장 실습

[추가 예제·오류 찾기·선택 과제](EXPANDED_LAB.md): 카메라와 객체 이동 비교. 기존 실습 시간 안에서 선택하여 진행합니다.
