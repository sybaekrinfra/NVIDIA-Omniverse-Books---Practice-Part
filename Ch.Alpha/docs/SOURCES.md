# 출처와 자료 처리

작성 기준일: 2026-10-26. 문서 안의 지침은 교육 참고 내용으로만 사용했습니다. 작업 범위는 사용자가 요청한 변경 Agenda와 Part별 실습 자료 구성입니다.

## 사용자 제공 자료

- 수정 Agenda: `교육/0 - 교육 커리큘럼/[한국인프라] 충북대학교 Omniverse 교육 Agenda - 수정본.pptx` 1~2페이지. Part 제목 및 시간 블록의 기준입니다.
- 사용자 메시지의 사전수요조사 요약: 초급 수준, CAD·Python·협업·Digital Twin 관심, 실습 50%. 실제 응답 원자료를 재집계한 결과는 아닙니다.
- `교육/1 - 교과 과정(2D)` 및 `3 - 세부 과정` PPTX: 교재 분배에 사용. 원본 수정 없음.
- `교육/2 - 교육 실습 자료/Ch.3`: STP, USD, 도면 3개 원본 복사.
- `교육/2 - 교육 실습 자료/Ch.2/LIVERPS_실습_usda파일`: 예제 전체 원본 복사.
- `교육/3 - 세부 과정/Scripts`: Stage 탐색·강체 낙하의 교육 방식 참고. 새 코드에서 기존 experimental API 예제를 직접 실행하지 않습니다.
- `D:/NVIDIA Omniverse Books/book/chapters/details/03_2_robot_asset_import.typ`: 자산 열기·Reference·Payload·Import 및 로컬 관리 설명 참고.

복사 파일의 SHA-256과 경로는 [ASSET_MANIFEST.csv](ASSET_MANIFEST.csv)에 기록합니다. 기존 CAD 및 도면의 권리 표기를 유지하며 새 라이선스를 임의 부여하지 않았습니다. 공개 저장소에 게시할 때는 제공 자료의 재배포 범위를 확인하세요. 기존 충북대 작성 시점에는 로컬 작업이었으며, 이번 Ch.Alpha 통합은 사용자 요청에 따라 상위 저장소에 커밋·Push합니다.

## 공식 웹 자료

| 출처 | 적용 부분 |
|---|---|
| [NVIDIA Legacy Tools](https://developer.nvidia.com/omniverse/legacy-tools) | Launcher·Nucleus Workstation 폐기 및 서버 방식 안내 |
| [CAD Converter User Manual](https://docs.omniverse.nvidia.com/extensions/latest/ext_cad-converter/manual.html) | CAD Import 기능·STEP 지원·변환 방식 |
| [Isaac Sim 설치](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/index.html) | 교육장 환경 준비 |
| [Isaac Sim 요구사항](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html) | 버전별 호환성 사전 확인 |
| [OpenUSD Referencing Layers](https://openusd.org/release/tut_referencing_layers.html) | Reference 및 defaultPrim 설명 |
| [Physics Developer Guide](https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/physics.html) | USD Physics API 구성 |
| [Physics Simulation Fundamentals](https://docs.isaacsim.omniverse.nvidia.com/latest/physics/simulation_fundamentals.html) | Rigid Body와 속성 접근 |
| [Learn OpenUSD Variant Sets](https://docs.nvidia.com/learn-openusd/latest/composition-basics/variant-sets.html) | compact / wide 배치 선택 |
| [OpenUSD Primvars](https://openusd.org/release/user_guides/primvars.html) | 면별 uniform displayColor |
| [UsdGeomPrimvar API](https://openusd.org/release/api/class_usd_geom_primvar.html) | 면 속성 및 보간 방식 |
| [UsdPhysics API](https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/latest/pxr/UsdPhysics.html) | 준비도 진단과 물리 속성 설정 |

웹 자료는 기능 확인 및 링크 제공에 사용했습니다. 웹 이미지·책 전체·외부 에셋을 다운로드해 재배포하지 않았습니다. 새 체크포인트, 한국어 실습 안내, 교육용 Python 및 가상 CSV는 이 과정에 맞게 작성했습니다.

## 통합 강의의 화면과 데이터

기존 사용자 교재에서 추출한 UI 화면 10개의 출처는 [manifest.json](../presentations/source/assets/manifest.json)에 기록했습니다. 기존 버전 화면 예시이며 새 실습 장면의 실행 검증 화면으로 사용하지 않습니다. 화면별 출처는 PPT 발표자 노트에도 있습니다.

온도·진동 CSV, 다중 장비 CSV, 면별 온도 CSV는 교육용 합성 데이터입니다. 온도 분포 예제는 CAE 결과를 읽는 형식을 설명하기 위한 기초 연습이며 실제 해석 결과나 현장 측정이 아닙니다. PPT의 온도 차트는 기본 CSV의 값과 교육용 판정 경계를 사용합니다.

## PSK 보강 (2026-10-29)

- 사용자 제공 `[한국인프라] Omniverse 교육 - Agenda(2D-6H) - PSK.pptx`의 2페이지: 09:00~16:30 시간 블록과 7개 Part를 확인했습니다. 원본 PPT 파일은 추가 배포하지 않습니다.
- 기존 충북대 자료는 전체 구성과 출처를 보존하여 가져왔습니다. 과거 설문·시간 배분은 PSK 교육생 조사 결과로 사용하지 않습니다.
- PSK 학습자 가이드·기록지·운영표·추가 미션, 단순 회전팔 USD/생성 코드, 초기화 경로 개선을 추가했습니다.
- ROS 2·Replicator는 상위 저장소 Ch.4·Ch.6 예제와 연결합니다. 실제 실행 여부는 강사 리허설 기록에서 구분합니다.
