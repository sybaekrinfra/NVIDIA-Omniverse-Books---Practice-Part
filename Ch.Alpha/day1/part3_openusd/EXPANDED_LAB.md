# D1P3 확장 실습 · USD 경로와 데이터 구조

이 실습은 기존 Part 시간 안에서 선택해 진행합니다. 기존 기본 실습을 10분, 확장 활동을 5분으로 배분합니다. 도전 과제는 조기 완료자 또는 교육 후 복습용입니다. 확장 활동을 기존 실습 뒤에 모두 추가하지 않습니다.

## 상황과 목표

**파일 경로와 Prim 경로 분류**을 수행합니다. 시작 파일은 `checkpoints/02_structured.usda`입니다. Python 예제는 Script Editor에서 `00_start_here.py`를 먼저 실행합니다. 원본 체크포인트는 저장하지 않고 결과를 outputs에 보관합니다.

## 가이드 실습

1. shared/assets/cad/BX200L-C001.usd와 /World/Equipment를 비교한다.
2. /World/Workpiece의 타입, Translate, 색 속성을 찾는다.
3. 장비를 담는 Xform과 실제 형상을 담는 Mesh를 구별한다.
4. Layer가 담은 의견과 Stage에서 합성한 결과를 한 문장으로 설명한다.

## 생각해 보기

Xform은 항상 보이는 형상인가?

팀원과 예상 결과를 적고 관찰 결과를 비교합니다. 해설은 강사와 함께 확인합니다.

## 자주 발생하는 문제

증상: 파일 경로를 GetPrimAtPath에 넣음

복구: Stage 내부 경로는 /World로 시작하는 Prim 경로를 사용한다.

## 선택 도전

Workpiece에 training:part_id 문자열을 만들고 타입 속성과 API schema의 차이를 설명한다.

## 제출 및 통과 기준

파일 경로/Prim 경로/Attribute 이름 분류표를 제출합니다. 결과만 보여주지 않고 설정 또는 데이터가 결과에 영향을 준 이유를 한 문장으로 설명하면 완료합니다.
