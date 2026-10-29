# Day 1·Day 2 통합 강의

[통합 PPT 열기](CBNU_Omniverse_Workshop_Integrated.pptx)

총 60장입니다. 흰 배경, 맑은 고딕, 실제 교재 화면과 코드 설명으로 구성했습니다. 본문·표·차트는 PowerPoint에서 편집할 수 있습니다. 화면 캡처는 이미지이며 교실 앱 버전에 맞는 화면으로 교체할 수 있습니다.

## 진행 순서

| 구분 | 페이지 | 내용 |
|---|---:|---|
| 시작 | 1~2 | 과정 소개와 학습 순서 |
| D1 P1 | 3~4 | 장면 구성과 첫 실행 |
| D1 P2 | 5~8 | UI, 객체와 카메라 조작 |
| D1 P3 | 9~13 | Stage·Prim·경로·속성 |
| D1 P4 | 14~19 | Layer·Reference·Payload·Variant |
| D1 P5 | 20~24 | CAD, 단위, Measure·Section·Pivot |
| D1 P6 | 25~28 | Layer 분업, Nucleus, 첫날 점검 |
| Day 2 시작 | 29 | 물리와 자동화 개요 |
| D2 P1 | 30~32 | Simulation Ready 준비도 |
| D2 P2 | 33~35 | CAD와 작업물의 역할별 계층 |
| D2 P3 | 36~39 | 질량·높이 비교 실험 |
| D2 P4 | 40~42 | 물리 설정과 바닥 통과 오류 |
| D2 P5 | 43~47 | Python 기초, 속성 변경, 반복 배치 |
| D2 P6 | 48~51 | 비동기 실행과 결과 기록 |
| D2 P7 | 52~58 | 상태 판정, 다중 장비, 온도 분포 선택 |
| 마무리 | 59~60 | 검토 기준과 제출 |

## 강의 준비

1. [환경 준비](../docs/SETUP.md)와 [리허설표](../docs/VALIDATION.md)로 교육장 버전을 확인합니다.
2. 각 Part의 기본 README와 EXPANDED_LAB을 함께 엽니다. PPT는 설명·시연용, 안내서는 실행 단계 확인용입니다.
3. [시간 배분](../docs/EXPANSION_GUIDE.md)에 맞춰 선택 문제를 고릅니다. 특히 55~56장의 다중 장비와 57장의 합성 온도 분포는 둘 중 하나를 팀 과제로 진행합니다.
4. PowerPoint 발표자 보기에서 노트를 확인합니다. [발표자 원고](LECTURE_NOTES.md)는 슬라이드별 해설이며, PPT 노트에는 Part별 진단 질문·예상 답·시간을 추가했습니다.

실행 가능한 전체 코드는 `scripts`에 있습니다. PPT의 짧은 코드는 설명용 발췌이므로 필요한 import와 초기화가 생략될 수 있습니다. Script Editor에서는 먼저 `00_start_here.py`를 실행합니다.

## 수정용 소스

`source/content.mjs`는 슬라이드 문구와 원고, `source/build_lecture.mjs`는 편집 가능한 PPT를 생성하는 코드입니다. `source/parts.json`은 Part 연결 정보, `source/slide_index.json`은 페이지 목록입니다. 기존 교재 화면의 출처는 `source/assets/manifest.json`에 있습니다.

학습자는 빌드 도구를 실행할 필요가 없습니다. 작성 환경에서는 제공된 `@oai/artifact-tool` 런타임과 Presentations 스킬 도구를 사용합니다. `ARTIFACT_TOOL_PATH`, `PRESENTATION_SKILL_DIR`, `CBNU_DECK_BUILD` 환경변수 지정 후 `build_lecture.mjs`를 실행합니다. 검증·최종화에는 `ARTIFACT_PYTHON`과 `RUNTIME_NODE_MODULES`도 지정하고 `finalize_lecture.mjs`를 실행합니다. 임시 렌더와 검증 기록은 저장소 밖 빌드 폴더에 둡니다.
