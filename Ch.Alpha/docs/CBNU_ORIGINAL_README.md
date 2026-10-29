# 충북대학교 기계공학부 Omniverse 실습

초급자를 위한 2일 과정입니다. CAD 장비가 놓인 공통 장면에 USD 구조, 작업물 물리 설정, Python 제어, 가상 상태 시각화를 차례로 추가합니다. 장비는 기존 BX200L CAD 형상을 재사용하며 관절 구동은 다루지 않습니다.

## 통합 강의와 확장 실습

- [Day 1·Day 2 통합 강의 PPT, 60장](../presentations/CBNU_Omniverse_Workshop_Integrated.pptx)
- [PPT 진행 순서와 Part별 페이지](../presentations/README.md), [발표자 원고](../presentations/LECTURE_NOTES.md)
- [13개 Part 확장 실습 구성 및 시간 배분](../docs/EXPANSION_GUIDE.md)
- [강사용 예상 답안과 복구 안내](../instructor/EXPANDED_ANSWERS.md)
- [팀별 미니 프로젝트](../docs/TEAM_PROJECT.md)

각 Part의 `README.md`는 기본 실습, `EXPANDED_LAB.md`는 비교·오류 복구·응용 문제입니다. 확장 문제는 기존 실습 시간 안에서 선택합니다. 하루 6시간 중 실습 180분을 유지하며 모든 도전 문제를 필수로 진행하지 않습니다.

## 먼저 시작하기

1. 저장소 전체를 내려받습니다. `checkpoints` 파일만 따로 옮기면 Reference 경로가 끊어집니다.
2. [환경 준비](../docs/SETUP.md)를 확인한 뒤 Isaac Sim에서 `checkpoints/01_layout.usda`를 엽니다.
3. Viewport의 카메라 선택에서 `/World/Camera`를 선택합니다. 또는 Stage에서 `/World` 선택 후 Frame Selection으로 전체를 봅니다.
4. 해당 Part의 README를 따라갑니다. Python을 사용하는 Part는 Script Editor에서 `scripts/00_start_here.py`의 ROOT 경로를 수정하고 먼저 실행합니다.
5. 단계가 막히면 [체크포인트 안내](../checkpoints/README.md)로 복구합니다. 결과는 `outputs`에 보관합니다.

## Part별 실습

| Day / Part | 내용 | 실습 안내 | 주요 파일 |
|---|---|---|---|
| 1 / 1 | Orientation | [안내](../day1/part1_orientation/README.md) | 환경·학습 목표 확인 |
| 1 / 2 | App UI / 조작 | [안내](../day1/part2_ui/README.md) | `01_layout.usda` |
| 1 / 3 | OpenUSD 설명 | [안내](../day1/part3_openusd/README.md) | `part.usda`, `assembly.usda` |
| 1 / 4 | USD 기능 | [안내](../day1/part4_usd_features/README.md) | `review.usda`, 기존 LIVERPS 예제 |
| 1 / 5 | CAD 및 기능 | [안내](../day1/part5_cad/README.md) | BX200L STP / USD |
| 1 / 6 | 구조화 / Nucleus | [안내](../day1/part6_collaboration/README.md) | `02_structured.usda` |
| 2 / 1 | Simulation Ready | [안내](../day2/part1_simready/README.md) | 준비도 체크리스트 |
| 2 / 2 | Import / Hierarchy | [안내](../day2/part2_hierarchy/README.md) | CAD Reference |
| 2 / 3 | 물리 개념 | [안내](../day2/part3_physics_concepts/README.md) | 물리 속성 비교 |
| 2 / 4 | Collider / Rigid Body / Mass | [안내](../day2/part4_physics_setup/README.md) | `02_apply_physics.py` |
| 2 / 5 | Script Editor / Python | [안내](../day2/part5_python/README.md) | `01`, `03` 스크립트 |
| 2 / 6 | 자동화 | [안내](../day2/part6_automation/README.md) | `04_automate_simulation.py` |
| 2 / 7 | Digital Twin 기초 | [안내](../day2/part7_digital_twin/README.md) | `05_replay_status.py`, CSV |

## 강사용 자료

- [전체 운영표 및 50% 실습 배분](../docs/CURRICULUM.md)
- [기존 교과 과정과 자료 재사용표](../docs/MATERIAL_MAP.md)
- [강사 진행·정답·평가 기준](../instructor/TEACHING_GUIDE.md)
- [학습자 실습 기록지](../docs/WORKSHEET.md)
- [출처와 배포 범위](../docs/SOURCES.md)
- [검증 결과와 리허설 항목](../docs/VALIDATION.md)
- [Git 저장소 운영](../docs/REPOSITORY.md)

`shared/assets/cad`에 기존 CAD·USD·도면을, `shared/assets/legacy_liverps`에 기존 USD 예제를 복사했습니다. 기존 교재의 위치는 재사용표에, 새 통합 강의는 `presentations`에 정리했습니다. ROS 2, Mobile Robot, 관절 제어, Replicator, Isaac Lab은 본 과정의 필수 실습에서 제외했습니다.

물리 실습은 바닥과 20cm 작업물의 강체 낙하입니다. CAD 장비 자체의 동역학 모델링이나 SimReady 인증을 의미하지 않습니다. Digital Twin 실습은 가상 CSV를 장비 속성과 색상에 연결하며 실제 센서·PLC·CAE 해석과 연결하지 않습니다.
