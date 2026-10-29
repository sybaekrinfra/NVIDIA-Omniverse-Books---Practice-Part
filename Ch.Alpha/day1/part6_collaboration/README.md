# Day 1 Part 6 · USD 구조화와 Nucleus 협업

배정 105분: 설명 53분, 실습 52분. 입력: `checkpoints/02_structured.usda`, `shared/assets/usd_basics`.

## 목표와 개념

장비 원본, 배치, 상태 변경을 서로 다른 Layer로 관리하는 이유를 설명합니다. Nucleus는 자산 공유와 권한 관리 환경이며 실제 서버 연결과 로컬 Layer 합성은 구별합니다.

## 공통 실습

1. 02를 열고 root Layer의 subLayer가 01을 가리키는지 확인합니다.
2. `/World/Equipment`에 연결된 CAD 파일과 `/World/Workpiece`의 역할을 구분합니다.
3. `shared/assets/usd_basics` 폴더 전체를 `outputs/team_demo`로 복사합니다.
4. 두 명이 역할을 나눕니다. A는 복사본 `assembly.usda`에서 ReferencePart의 Translate X를 -2로 수정합니다. B는 복사본 `review.usda`에서 해당 부품의 색을 보라색으로 수정합니다. 같은 파일을 동시에 덮어쓰지 않습니다.
5. B의 review를 열거나 Reload하여 A의 위치와 B의 색이 함께 반영되는지 확인합니다.
6. review를 Flatten하여 저장한 결과와 원본 폴더 구조를 비교하고, 원본 변경이 Flatten 결과에 자동 반영되지 않는 이유를 설명합니다.

## Nucleus 서버가 준비된 경우

1. 강사가 지정한 서버와 개인 계정으로 접속합니다. 비밀번호는 저장소에 기록하지 않습니다.
2. 교육용 팀 경로에 `team_demo` 폴더 전체를 올려 상대 경로를 유지합니다.
3. 다른 계정에서 review를 열고 참조가 정상인지 확인합니다.
4. A가 assembly를 수정·저장한 뒤 B가 Reload하여 결과를 확인합니다.
5. 읽기 전용 계정의 저장 제한을 확인합니다. Live Session은 앱·서버 지원을 사전 검증한 경우에만 강사가 시연합니다.

서버가 없으면 공통 실습까지 완료하고 “Nucleus 개념 설명 / 로컬 분업 실습”으로 기록합니다.

## 완료 확인

제출: 팀별 역할표, 합성 결과 화면, 상대 경로 패키지, 원본과 override의 차이. 협업 폴더를 통째로 다른 위치로 복사한 뒤 재열기까지 확인합니다.

오늘의 공통 장면 결과는 `checkpoints/README.md`의 저장 코드로 `outputs/day1_result.usda`에 저장할 수 있습니다.

## 확장 실습

[추가 예제·오류 찾기·선택 과제](EXPANDED_LAB.md): 배치 수정과 검토 색 동시 반영. 기존 실습 시간 안에서 선택하여 진행합니다.
