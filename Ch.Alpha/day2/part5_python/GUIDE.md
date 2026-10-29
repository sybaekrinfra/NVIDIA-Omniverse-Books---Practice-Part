# Day 2 Part 5 · Script Editor와 Python API

배정 60분: 설명 30분, 실습 30분. 입력: `03_physics.usda`, scripts 00, 01, 03.

## Python 초급 안내

`import`는 기능 가져오기, 변수는 값에 붙인 이름, 함수는 반복 가능한 동작입니다. 문자열 경로는 따옴표 안에 씁니다. `GetPrimAtPath`는 Prim을 찾고 `GetAttribute`는 속성을 찾으며 `Set`은 값을 씁니다. 들여쓰기를 유지하세요.

## 따라하기

1. 03 체크포인트를 엽니다. 00의 ROOT를 확인하고 실행합니다.
2. 01을 실행하여 출력된 경로·단위·축을 기록합니다.
3. 다음 코드를 Script Editor에서 실행합니다.

```python
from cbnu_lab import current_stage
s = current_stage()
p = s.GetPrimAtPath("/World/Workpiece")
print(p.GetAttribute("xformOp:translate").Get())
print(p.GetAttribute("physics:mass").Get())
```

4. Stop 상태에서 03 스크립트의 HEIGHT_M을 1.5에서 2.0으로 바꿔 실행합니다. GUI의 Translate Z가 2인지 확인합니다.
5. MASS_KG를 5.0으로 바꾸고 실행해 Property의 Mass를 확인합니다.
6. HEIGHT_M=1.5, MASS_KG=1.0으로 복구합니다. 출력 경로를 고의로 틀린 코드로 바꿀 때는 읽기 실험에 한정하고 유효 Prim 여부를 확인합니다.

## 완료 확인

제출: 두 변수 변경 전후 값, Console 출력, GUI 값의 일치 여부. 잘못된 경로 오류와 ROOT 설정 오류를 구별하면 통과합니다.

Python으로 좌표를 쓰는 것과 물리 엔진이 강체를 움직이는 것은 구별합니다. 이번 속성 변경은 Stop 상태에서 수행합니다.

## 확장 실습

[추가 예제·오류 찾기·선택 과제](EXPANDED_LAB.md): 6개에서 12개 작업물로 확장. 기존 실습 시간 안에서 선택하여 진행합니다.
