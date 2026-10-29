# 기존 교육 자료 배치표

아래 경로는 원래 `교육` 폴더 기준입니다. 슬라이드 번호는 PPTX 내부 순서(1부터)입니다. 기존 발표자료 원본은 보존했습니다. 새로 구성한 [통합 강의 60장](../presentations/README.md)은 이 저장소의 실습 순서를 따릅니다. 기존 교재 화면 10개를 활용했으며 원본 파일·슬라이드 번호는 [화면 출처 기록](../presentations/source/assets/manifest.json)에 있습니다.

## 발표자료 약칭

| 약칭 | 원본 |
|---|---|
| 소개 | `1 - 교과 과정(2D)/0.0 - [한국인프라] NVIDIA Omniverse Platform 소개.pptx` |
| 사례 | `1 - 교과 과정(2D)/0.1 - [한국인프라] NVIDIA Omniverse 활용과 Digital Twin 구축 사례.pptx` |
| 설치 | `1 - 교과 과정(2D)/0.2 - [한국인프라] Omniverse와 IsaacSim 설치 방법.pptx` |
| UI | `1 - 교과 과정(2D)/1 - [한국인프라] Omniverse 세부 설명.pptx` |
| USD | `1 - 교과 과정(2D)/2 - [한국인프라] OpenUSD 설명자료.pptx` |
| Isaac | `1 - 교과 과정(2D)/3 - [한국인프라] Isaac SIm 세부 설명.pptx` |
| 물리 | `1 - 교과 과정(2D)/4 - [한국인프라] 물리 설정 with 자동차.pptx` |
| 6H | `6H - [한국인프라] Omniverse와 Isaac Platform 교육 메인자료.pptx` |

## Part별 분배 및 수정 필요점

| Part | 사용할 교재 부분 | 실습 재사용 및 새 자료 | 강의 조정 |
|---|---|---|---|
| D1 P1 | 소개 2~4, 사례 3, 설치의 환경 확인 | SETUP, WORKSHEET | 실제 DT 사례와 수업의 가상 데이터 범위 구분 |
| D1 P2 | UI 8~20 | 공통 01 장면 신규 | 기존 UI 기본 교육 유지 |
| D1 P3 | USD 3~10, 13~16 | usd_basics 신규 | Stage·Prim·Property 개념 유지 |
| D1 P4 | USD 19~32, 선택 36~39 | 기존 Ch.2 LIVERPS + 단순 예제 | 기본 USD 교육 유지, 심화 우선순위는 선택 |
| D1 P5 | 6H 13~14, UI 29~32 | 기존 Ch.3 STP·USD·도면 복사 | Import·Measure·Pivot·Section 중심 |
| D1 P6 | UI 14, 23~24; USD 42~47 | review Layer, 로컬 분업 | Curve Editor/OmniGraph 중심에서 협업으로 전환 |
| D2 P1 | 6H 13~16, Isaac 24 | SimReady 체크표 | Joint·Drive 단계 제외 |
| D2 P2 | Isaac 14,16~20,24 | 기존 CAD 및 새 래퍼 장면 | URDF 대신 CAD/USD 사용 |
| D2 P3 | 물리 6,15~17 | 전후 체크포인트 | 자동차 동역학 대신 단순 낙하 |
| D2 P4 | 6H 15, 물리 15~17 | add_physics와 03 장면 신규 | Articulation·Joint·Drive 심화 제외 |
| D2 P5 | 기존 Scripts의 01/02 개념 | 경로 탐색·변수 변경 코드 신규 | Python 기초 문법·API 설명 추가 |
| D2 P6 | UI 33의 Timeline 개념 | 비동기 실행·CSV 기록 신규 | 기존 실험 API 의존을 줄인 코드 |
| D2 P7 | 사례 3, 선택 CFD 자료 | 가상 CSV·상태 판정·시각화 신규 | 실제 설비 연동과 구별, Replicator 대체 |

기존 `3 - 세부 과정/Scripts/03_normalizer_xform.py`는 변환 스택을 다시 쓰므로 초급 필수 실습에 넣지 않았습니다. `04_isaac_physics.py`의 강체 낙하 교육 개념은 재사용하되 이번 코드는 표준 USD Physics API로 새로 작성했습니다. 05~07의 로봇·Replicator 예제는 제외합니다.

## 기존 자산 처리

| 원본 | 처리 |
|---|---|
| `2 - 교육 실습 자료/Ch.2/LIVERPS_실습_usda파일` | 파일 전체를 shared/assets/legacy_liverps로 복사해 내부 참조 유지 |
| `2 - 교육 실습 자료/Ch.3`의 3개 파일 | shared/assets/cad로 복사, 장비 형상 및 CAD 변환에 활용 |
| Ch.2 KukaArm1 | 필수 제외, 기본 USD는 더 단순한 자산 사용 |
| Ch.4~5 로봇·ROS 2 | 필수 제외 |
| Ch.6 합성 데이터 / Ch.7 RL | 필수 제외 |
| `3 - 세부 과정/CFD` 3개 PPT | D2 P7 선택 개념 시연, CAE 실습 필수화하지 않음 |

## D 드라이브 교재 활용

`D:/NVIDIA Omniverse Books/book/chapters/details/03_2_robot_asset_import.typ`의 Open/Reference/Payload/Import 구별과 로컬 에셋 관리 설명을 참고했습니다. 교재의 버전 표기는 SETUP의 사전 환경 확정 절차와 함께 사용합니다. 교재 전체나 대용량 이미지·빌드 산출물은 새 저장소로 복제하지 않았습니다.
