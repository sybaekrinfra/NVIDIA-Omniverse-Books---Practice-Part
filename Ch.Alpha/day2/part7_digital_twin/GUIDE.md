# Day 2 Part 7 · 가상 데이터 기반 Digital Twin 기초

배정 105분: 설명 53분, 실습 52분. 입력: `03_physics.usda`, `shared/data/equipment_status.csv`, `05_replay_status.py`.

## 목표와 데이터 계약

가상 장비 값을 읽고 판정한 뒤 USD 속성과 표시구에 연결합니다. CSV의 `time_s`는 증가하는 재생 시각, `temperature_c`는 섭씨 온도, `vibration_mm_s`는 진동 속도입니다. 8개 샘플은 교육용 합성 데이터입니다.

| 판정 | 조건(OR) | 표시 |
|---|---|---|
| ALARM | 온도 ≥ 80 또는 진동 ≥ 7 | 빨강 |
| WARNING | ALARM이 아니면서 온도 ≥ 60 또는 진동 ≥ 4 | 주황 |
| NORMAL | 나머지 | 녹색 |

이 임계값은 교육용이며 실제 장비 안전 기준이 아닙니다. CAD 장비 전체 색을 바꾸지 않고 별도 StatusLamp와 Equipment의 custom 속성을 사용합니다.

## 따라하기

1. 03 장면을 열고 Timeline Stop 상태를 확인합니다.
2. CSV를 열어 각 행의 예상 상태를 기록합니다. 80°C 경계와 7mm/s 경계가 포함되어 있습니다.
3. 05를 실행합니다. 0~7초 간격으로 표시구가 녹색→주황→빨강→녹색으로 바뀌는지 봅니다.
4. `/World/Equipment`의 `training:state`, `training:temperature_c`, `training:vibration_mm_s`, `training:source`를 확인합니다. Custom 속성 표시가 없으면 Console 출력을 확인합니다.
5. 자동 저장된 `outputs/day2_final.usda`를 다시 열어 마지막 NORMAL 상태와 source=`SYNTHETIC_CSV`를 확인합니다.
6. CSV를 백업한 후 마지막 행 온도를 85로 바꾸어 다시 실행합니다. 최종 ALARM과 빨간 표시구를 확인합니다. 결과를 별도 이름으로 저장하고 CSV는 복원합니다.
7. 선택 과제: 온도 59.9, 60, 79.9, 80과 진동 3.9, 4, 6.9, 7의 경계 결과를 설명합니다. 잘못된 시간 순서와 음수 진동이 거부되는지도 확인합니다.

## 완료 확인 및 제출

완성 USD, 수정 CSV 사본, 정상/주의/경보 화면, 상태 판정표를 제출합니다. 색과 숫자가 일치하고 실제 설비 데이터가 아니라는 점을 설명하면 통과합니다.

최종 고정 예시는 `04_status.usda`의 ALARM입니다. 원본 CSV 전체 재생 결과는 NORMAL이므로 두 결과가 달라도 오류가 아닙니다.

## CAE 관심자를 위한 선택 설명

기존 `3 - 세부 과정/CFD` 발표자료로 해석 field와 장비 scalar 값의 차이를 설명합니다. 여기의 단일 온도 값 색상 표시는 CAE 결과 Import나 유동·온도장 해석을 수행하지 않습니다. 실제 CAE 확장은 데이터 형식, 좌표계, 단위, field mapping을 확보한 후 별도 교육으로 구성합니다.

## 확장 실습

[추가 예제·오류 찾기·선택 과제](EXPANDED_LAB.md): 세 장비의 정상·이상·결측·지연 표시. 기존 실습 시간 안에서 선택하여 진행합니다.
