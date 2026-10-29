# Ch.Alpha 검증 기록

## PSK 보강 검사 · 2026-10-29

환경: Linux, 설치된 Isaac Sim의 `python.sh`, 내장 OpenUSD 0.25.11. 아래 명령은 Isaac Sim 설치 폴더를 기준으로 실행했습니다.

```bash
./python.sh extsUser/NVIDIA-Omniverse-Books---Practice-Part/Ch.Alpha/tools/validate.py
./python.sh extsUser/NVIDIA-Omniverse-Books---Practice-Part/Ch.Alpha/tools/validate_expanded.py
./python.sh extsUser/NVIDIA-Omniverse-Books---Practice-Part/Ch.Alpha/tools/validate_psk.py
```

- PASS: USD 29개 로드 및 의존 경로, 물리 API, 재실행, 속성 수정, CSV 경계, 합성·Flatten.
- PASS: Variant, 두 오류 장면의 진단/복구, 4개 배치 크기, 12개 장비 데이터, 결측/지연, 두 온도장, 비교 장면 강체 3개.
- PASS: 새 관절의 Body 연결·세계/로컬 앵커 일치·회전축·제한·Drive 속성과 목표값 변경, Markdown 파일 링크, 중첩 Git 없음.
- PASS: 모든 Python 구문 검사. 기존 자산 및 presentations 40개 파일을 원본과 SHA-256 비교하여 동일함을 확인.
- 미검증: Script Editor 자동 경로 탐색의 실제 GUI 실행, 화면 렌더링, PhysX 낙하·관절 운동, ROS 2 연결, Replicator 이미지 출력, STEP 변환, Nucleus.

정적 검사 성공을 실제 시뮬레이션 성공으로 해석하지 않습니다. PSK 현장 리허설과 실행 여부는 [강사 운영표](../instructor/PSK_DAY2_RUNBOOK.md)에 기록합니다. 이전 자료의 검증 이력은 아래에 보존합니다.

---

# 검증 결과 및 교육장 리허설

검사일: 2026-10-26. 검사 환경: Windows, Python 3.13.2, 별도 가상환경 usd-core 26.11. 이 버전은 패키지 구조 검사에 사용한 것이며 교육용 Isaac Sim의 내장 USD 버전을 의미하지 않습니다.

## 수행한 검사

- 신규 및 복사된 USD 28개 파일의 OpenUSD 로드 성공(확장 장면 7개 포함).
- USD 의존 파일 탐색에서 누락된 Reference/Layer/외부 자산 없음.
- meter·Z-up·defaultPrim, 작업물과 바닥의 Physics API 확인.
- 공통 장면의 CAD 하위에서 기존 강체·관절·충돌이 활성화되지 않는지 확인. 원본은 보존하고 local override로 제거.
- 물리 설정 함수를 두 번 적용해도 Prim이 중복 생성되지 않음.
- Python 함수로 높이 2m·질량 5kg 변경 후 USD 속성값 확인.
- CSV 8개 상태와 온도·진동 임계값 경계, 비정상 수치 거부 확인.
- 상태 반영 후 Flatten 장면 재열기, 최종 NORMAL 속성 확인.
- review Layer 색상 override 및 Payload load/unload 확인.
- Python 구문 검사. Kit 전용 wrapper는 구문 검사만 수행.
- 원본 복사 자산 SHA-256 비교는 ASSET_MANIFEST.csv 참조.

발견 및 수정: 기존 telemetryAttribute.usda는 Python 코드라 새 복사본의 확장자만 .py로 변경했습니다. Windows usd-core에서 한글 경로에 새 USD 생성 오류가 있어 체크포인트는 영문 임시 경로에서 생성 후 요청 폴더로 옮겼습니다. 학습자 결과 저장 함수는 UTF-8 텍스트 쓰기를 사용합니다. 환경별 경로 문제에는 영문 실행 경로를 권장합니다.

## 아직 수행하지 않은 검사

확장 자료는 `python tools/validate_expanded.py`로 별도 검사했습니다. Variant 배치 간격, 단위·바닥 충돌 오류의 진단과 복구, 배치 개수 변경과 재실행, 12개 장비 데이터 판정, 결측값 차단, 3초 신선도 경계, 잘못된 CSV 거부, 24개 면의 색 보간 및 합성 온도 범위가 통과했습니다. 비교 장면의 활성 동적 강체는 A/B/C입니다. 이 결과는 USD 구조와 Python 로직 검사입니다.

Isaac Sim GUI 렌더링, PhysX 실제 낙하, Timeline 비동기 코드 실행, STEP 변환, Nucleus 연결은 이 작업 환경에서 검증하지 않았습니다. OpenUSD 검사를 통과했다는 사실이 이 동작들의 성공을 보장하지 않습니다.

## 강사 리허설 기록

| 검사 | 통과 조건 | 결과 / 버전 / 담당자 |
|---|---|---|
| 앱 환경 | 같은 Isaac Sim 버전과 지원 GPU/드라이버 | 미확인 |
| 01 장면 | CAD·작업물·표시구·카메라 정상 표시 | 미확인 |
| CAD Import | STP 변환 또는 제공 USD 대체 확정 | 미확인 |
| 보조 도구 | Measure/Pivot/Section 사용 또는 대체 확정 | 미확인 |
| Layer 협업 | 위치와 색 override 동시 반영 | 미확인 |
| Nucleus | 서버/계정/권한 정상 또는 로컬 대체 확정 | 미확인 |
| 03 물리 | 작업물 낙하·바닥 접촉·Stop 복원 | 미확인 |
| 04 자동화 | 2개 조건 실행 및 CSV 2행 | 미확인 |
| 05 상태 재생 | 8개 데이터·표시 색 일치, 마지막 NORMAL | 미확인 |
| 저장 | day2_final 재열기 및 속성 유지 | 미확인 |
| 확장 Variant / 배치 | compact·wide 전환, 6개→12개 재배치 | 미확인 |
| 비교 낙하 | A/B 질량 비교, C의 높은 초기 위치 | 미확인 |
| 오류 복구 | scale 및 Ground 활성값 수정 후 관찰 | 미확인 |
| 다중 상태 | 12행 보고서, 결측·지연 표시와 최종 상태 | 미확인 |
| 합성 온도 | 24면 색, 두 CSV에 같은 20~100°C 범례 | 미확인 |

재검사 명령: usd-core가 설치된 별도 환경에서 `python tools/validate.py`. Isaac Sim 내장 Python에 검사 패키지를 임의 설치하지 않습니다.
