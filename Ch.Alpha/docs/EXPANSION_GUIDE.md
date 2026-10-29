# 확장판 이용 안내

이번 확장판은 13개 Part의 설명·판단·오류 복구 활동을 보강하고 Day 1·Day 2를 60장 통합 강의 PPT로 연결합니다. 기존 필수 흐름과 하루 6시간/실습 3시간 배분을 유지합니다.

## 새 자료

| 자료 | 용도 |
|---|---|
| presentations/CBNU_Omniverse_Workshop_Integrated.pptx | 두 날을 이어 진행하는 통합 강의, 편집 가능한 본문·표·차트 |
| presentations/LECTURE_NOTES.md | 슬라이드별 강의 원고, PPT 노트에는 Part별 질문·답안 추가 |
| 각 Part의 EXPANDED_LAB.md | 상황, 단계, 질문, 오류 복구, 도전 과제 |
| instructor/EXPANDED_ANSWERS.md | 질문 답안과 시간 운영 |
| docs/TEAM_PROJECT.md | 팀별 선택 프로젝트와 제출 기준 |
| checkpoints/05~11 | 새 실습 및 의도적으로 만든 오류 장면 |
| scripts/07~11 | Variant, 진단, 반복 배치, 다중 상태, 온도 분포 |

## 장면과 실행 연결

| 장면 | 관련 Part | 실행 | 결과 |
|---|---|---|---|
| 05_layout_variants.usda | D1 P4 | 07_layout_variant.py | compact / wide 전환 |
| 06_physics_comparison.usda | D2 P3 | UI Play / Stop | A·B·C의 질량/높이 비교 |
| 07_batch_layout.usda | D2 P5 | 09_batch_layout.py | 행·열·간격을 바꾸는 반복 배치 |
| 08_multi_equipment.usda | D2 P7 선택 A | 10_multi_equipment.py | 3개 장비, 12행 상태 보고서 |
| 09_thermal_field.usda | D2 P7 선택 B | 11_thermal_field.py | 24면 가상 온도 분포 |
| 10_fault_units.usda | D1 P5 | 08_check_readiness.py | 1,000배 크기 오류 진단 |
| 11_fault_collision.usda | D2 P4 | 08_check_readiness.py + GUI 수정 | 비활성 바닥 충돌 복구 |

10·11은 의도적으로 잘못된 값을 담은 교육용 장면입니다. 배포 파일이 정상이어도 진단 결과에 CHECK가 나옵니다. 원본을 고치지 말고 복사본 또는 메모리 편집 후 재열기로 복구하세요.

Python은 기존과 같이 00_start_here.py를 먼저 실행합니다. 새 모듈을 추가한 이후에는 앱을 재시작하거나 00을 다시 실행하여 경로를 준비합니다. 비동기 재생은 서로 겹쳐 실행하지 않고 장면을 바꾸기 전에 06_stop_tasks.py로 종료합니다.

## 시간 안에서 선택하는 방식

| Part | 기본 실습 | 확장 활동 | 실습 합계 |
|---|---:|---:|---:|
| D1 P1 | 6 | 4 | 10 |
| D1 P2 | 12 | 8 | 20 |
| D1 P3 | 10 | 5 | 15 |
| D1 P4 | 24 | 14 | 38 |
| D1 P5 | 25 | 20 | 45 |
| D1 P6 | 32 | 20 | 52 |
| Day 1 합계 | 109 | 71 | 180 |
| D2 P1 | 8 | 7 | 15 |
| D2 P2 | 18 | 12 | 30 |
| D2 P3 | 9 | 6 | 15 |
| D2 P4 | 15 | 8 | 23 |
| D2 P5 | 18 | 12 | 30 |
| D2 P6 | 10 | 5 | 15 |
| D2 P7 | 30 | 22 | 52 |
| Day 2 합계 | 108 | 72 | 180 |

단위는 분입니다. 기존 설명 시간에는 예측 질문과 결과 해설을 포함합니다. 교육생이 기본 실습에서 지연되면 확장 활동을 강사 시연이나 복습으로 넘깁니다. D2 P7의 다중 장비와 온도 분포는 둘 중 하나만 선택합니다.

## 발표자료 사용

PPT 본문은 강의실 화면용으로 정리하고 상세 답안과 실행 주의는 발표자 노트에 넣었습니다. 기존 교재 화면 10개는 원본 이미지로 활용했습니다. 이 이미지는 현재 교육장 UI나 새 실습의 실행 검증 캡처가 아닙니다. 교육장 버전에서 실행한 캡처를 추가할 때는 해당 페이지 이미지만 교체할 수 있습니다.

기존 교재는 심화 참고로 유지합니다. 새 통합 교재를 기본 진행 자료로 사용하면 기존 파일 사이를 오가며 강의할 필요를 줄일 수 있습니다. 원본 PPT와 Agenda는 변경하지 않았습니다.
