# Ch.Alpha · Omniverse 실습 워크숍

기존 충북대 워크숍의 장면·스크립트·강의 자료를 옮기고 **PSK 2일차 비개발자 실습 경로**를 추가했습니다. 1일차를 마친 교육생은 아래 순서로 시작하세요.

1. 강사: [PSK 2일차 6시간 운영표](instructor/PSK_DAY2_RUNBOOK.md)에서 리허설과 대체 경로를 확인합니다.
2. 교육생: [2일차 실습 가이드](docs/PSK_DAY2_LABS.md)를 열고 실습 1부터 진행합니다.
3. [기록지](docs/PSK_DAY2_WORKSHEET.md)에 예상 → 관찰 → 설명을 적습니다.
4. 먼저 끝난 팀은 [추가 미션](docs/PSK_BONUS_MISSIONS.md)을 선택합니다.
5. 막히면 해당 실습의 복구 파일을 다시 엽니다. [환경 준비](docs/SETUP.md), [검증 기록](docs/VALIDATION.md)을 참고합니다.

**전체 저장소 또는 Ch.Alpha 전체를 복사**하세요. checkpoints만 옮기면 상대 Reference가 끊어집니다. Script Editor 초기화는 `scripts/00_start_here.py`를 실행합니다. 장면을 checkpoints에서 열었다면 Ch.Alpha 경로를 자동으로 찾습니다. 찾지 못할 때만 ROOT를 수정합니다.

## 포함 자료와 적용 범위

| 경로 | 용도 |
|---|---|
| docs/PSK_* | 이번 PSK 수업용 학습자 가이드·기록지·추가 미션 |
| instructor/PSK_DAY2_RUNBOOK.md | Agenda 대응, 시간 조절, 강사 해설·리허설 |
| day1/, day2/ | 기존 충북대 기본·확장 실습 (기존 Part 번호 유지) |
| checkpoints/ | 독립적으로 시작·복구할 수 있는 USD 장면 |
| scripts/, shared/ | 실행 예제, CAD, 합성 CSV, 공통 함수 |
| presentations/ | 기존 충북대 60장 통합 PPT 및 제작 소스 |
| tools/ | 강사용 생성·검증 도구 |
| outputs/ | 개인 결과 저장 위치 (Git 제외) |

기존 PPT와 `docs/CURRICULUM.md`는 **충북대 편성**입니다. PSK의 시간·오후 Part 번호는 새 운영표를 우선하세요. 첨부 PSK Agenda 자체는 복제하지 않았습니다. [출처](docs/SOURCES.md)와 [통합 이력](docs/REPOSITORY.md)을 참고하세요.

새 경로는 GUI 조작, 제공 코드의 숫자 변경, 짝별 설명으로 완주하도록 설계했습니다. ROS 2 연결·Replicator 렌더는 강사 PC에서 사전 검증 후 진행합니다. 온도장은 합성 데이터이며 실제 CAE 해석을 수행하지 않습니다. 기존 BX200L은 시각 참고용이고 관절 실습은 별도의 단순 회전팔 장면을 사용합니다.

기존 과정 전체 안내: [충북대 원본 안내](docs/CBNU_ORIGINAL_README.md).
