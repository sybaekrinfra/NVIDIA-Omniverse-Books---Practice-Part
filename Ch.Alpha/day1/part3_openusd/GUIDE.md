# Day 1 Part 3 · OpenUSD 설명

배정 30분: 설명 15분, 관찰 실습 15분. 입력: `shared/assets/usd_basics/part.usda`, `assembly.usda`.

## 목표와 개념

Prim 경로는 장면 내부 주소이고 파일 경로는 디스크 주소입니다. Reference는 자산을 다른 Prim 아래에 합성합니다. Payload는 명시적으로 로드·언로드할 수 있는 자산 연결입니다. `defaultPrim`은 참조할 Prim을 생략했을 때 사용할 진입점입니다.

## 따라하기

1. 텍스트 편집기로 `part.usda`를 열어 defaultPrim과 `/Part`의 Cube 정의를 찾습니다.
2. 앱에서 `assembly.usda`를 엽니다. `/World/ReferencePart`와 `/World/PayloadPart`를 찾습니다.
3. 두 Cube의 형상과 색은 같지만 Translate가 다른 이유를 설명합니다.
4. 파일에서 `@part.usda@`를 찾아 상대 파일 경로라고 기록합니다.
5. 강사 설명에 따라 PayloadPart를 unload한 뒤 load합니다. 해당 메뉴가 없으면 다음 Part의 Python 예제를 강사가 실행합니다.

## 완료 확인

기록지에 `Stage / Layer / Prim / Reference / Payload`를 한 문장씩 정의합니다. Payload 언로드 후 사라지는 형상은 PayloadPart이며 ReferencePart는 남습니다.

이번 Part는 개념 관찰입니다. LIVERPS의 모든 강도 규칙을 암기하도록 요구하지 않습니다.

## 확장 실습

[추가 예제·오류 찾기·선택 과제](EXPANDED_LAB.md): 파일 경로와 Prim 경로 분류. 기존 실습 시간 안에서 선택하여 진행합니다.
