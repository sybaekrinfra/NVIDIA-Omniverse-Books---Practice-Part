# 단계별 시작 및 복구 장면

| 파일 | 시작 위치 | 포함 내용 |
|---|---|---|
| 01_layout.usda | Day 1 Part 2 | CAD 장비 Reference, 작업물, 바닥, 상태 표시구, 카메라 |
| 02_structured.usda | Day 1 Part 6 / Day 2 Part 1~4 | 01을 subLayer로 연결한 편집 Layer |
| 03_physics.usda | Day 2 Part 5~7 | 02에 작업물 강체·충돌·1kg 질량, 바닥 충돌, 중력 추가 |
| 04_status.usda | 최종 결과 예시 / 복구 | 03에 4초 시점 ALARM(80°C) 상태 추가 |
| 05_layout_variants.usda | Day 1 Part 4 확장 | compact / wide 배치 비교 |
| 06_physics_comparison.usda | Day 2 Part 3 확장 | 질량·높이가 다른 A/B/C 작업물 |
| 07_batch_layout.usda | Day 2 Part 5 확장 | 2행×3열 배치, Python으로 개수 변경 |
| 08_multi_equipment.usda | Day 2 Part 7 선택 | E01~E03 단순 장비 표시구, 가상 CSV 연결 |
| 09_thermal_field.usda | Day 2 Part 7 선택 | 24개 면에 합성 온도 분포 표시 |
| 10_fault_units.usda | Day 1 Part 5 확장 | 의도적으로 잘못 설정한 CAD scale |
| 11_fault_collision.usda | Day 2 Part 4 확장 | 의도적으로 비활성화한 바닥 충돌 |

04는 경고 상태를 한눈에 보는 고정 예시입니다. CSV 전체 재생은 7초 시점 NORMAL로 끝납니다.

05~11은 별도 비교·응용 장면입니다. 번호 순서대로 누적 편집하는 과정이 아닙니다. 각 Part의 `EXPANDED_LAB.md`에 지정한 장면을 열고 실행합니다. 10과 11은 오류 찾기 문제이므로 진단표에서 일부 CHECK가 나오는 것이 의도한 초기 상태입니다.

원본 CAD USD에는 관절·강체·충돌 설정이 들어 있습니다. 01 장면의 local override에서 해당 API를 제거하고 Joint Prim을 비활성화하여 장비를 시각 참조로만 사용합니다. 원본 CAD USD는 변경하지 않았습니다. CAD를 직접 Open한 화면과 공통 장면의 물리 설정은 다릅니다.

체크포인트 전체와 `shared`의 상대 위치를 유지하세요. 배포 원본을 수정했다면 Git 복구 또는 배포본 재복사 후 엽니다. 결과를 보존하려면 Script Editor에서 다음을 실행합니다.

```python
from cbnu_lab import current_stage, save_result
save_result(current_stage(), "day1_result.usda")
```

이는 의존 경로 없이 열 수 있는 **Flatten 제출본**입니다. Layer·Reference 구조는 체크포인트 원본에 유지됩니다. 협업 제출에는 Flatten 대신 저장소 내 원래 폴더 구조를 함께 보관합니다.

## PSK 추가 장면

`12_joint_drive.usda`: 외부 자산 없는 1축 회전팔. `/World/Hinge`의 Z축·-60~60도 제한·angular Drive를 비교합니다. [실습 4](../docs/PSK_DAY2_LABS.md) 참고. 원본 CAD 로봇 관절 모델과 무관합니다.
