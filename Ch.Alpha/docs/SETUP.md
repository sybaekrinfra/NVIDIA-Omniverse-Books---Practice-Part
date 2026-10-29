# 환경 준비와 실행

## 기준

기존 설치 교재는 Isaac Sim 6.0.1을 기준으로 작성되어 있습니다. 이 패키지는 `pxr.Usd`, `UsdGeom`, `UsdPhysics`와 Kit Script Editor를 사용하도록 작성했습니다. 교육장 앱 버전·GPU·드라이버를 동일하게 맞추고 아래 리허설을 마친 버전을 확정하세요. GUI 및 물리 런타임 검증 상태는 [VALIDATION](VALIDATION.md)에 있습니다.

1. 강사가 공식 [요구사항](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html)과 [설치 안내](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/index.html)를 확인합니다. 설치 교재의 숫자를 최신 기준으로 간주하지 않습니다.
2. 설치된 Isaac Sim을 실행하고 빈 장면, Stage, Property, Content, Script Editor를 확인합니다. Script Editor 메뉴가 없으면 Extensions에서 `omni.kit.window.script_editor`를 검색합니다. 메뉴 위치는 앱 버전에 따라 다릅니다.
3. `checkpoints/01_layout.usda`를 엽니다. 장비·파란 작업물·녹색 표시구가 보이는지 확인합니다. 외부 에셋 다운로드는 이 장면의 필수 조건이 아닙니다.
4. 실습 전 원래 작업하던 Stage를 저장하세요. File > Open은 현재 장면을 바꿉니다. 배포 체크포인트는 저장하지 않고 다음 단계로 열어 사용합니다.

## Python 사용법

일반 PowerShell Python에서 `scripts/01~06`을 실행하지 않습니다. Isaac Sim의 Script Editor에서 파일을 열거나 내용을 붙여 넣고 실행하세요.

1. PSK 경로는 먼저 checkpoints의 장면을 연 뒤 `scripts/00_start_here.py`를 실행하면 경로를 자동으로 찾습니다. 자동 탐색 실패 시 ROOT에 Ch.Alpha 경로를 지정합니다. 실행용 복사본은 `C:/omniverse/cbnu-workshop`처럼 영문 경로에 두는 것을 권장합니다. Windows usd-core 검사에서 한글 경로의 새 USD 파일 생성 오류를 확인했습니다. Isaac Sim에서도 경로 오류가 발생하면 저장소 전체를 영문 경로로 복사하세요. 수동 지정 예: `ROOT = Path(r"C:/omniverse/NVIDIA-Omniverse-Books---Practice-Part/Ch.Alpha")`.
2. 00 실행 후 01을 실행해 Stage 경로를 확인합니다. `cbnu_lab` import 오류는 00 미실행 또는 ROOT 오류입니다.
3. 02, 03은 Timeline **Stop** 상태에서 실행합니다. Pause 상태와 구분하세요.
4. 04가 끝난 후 05를 실행합니다. 중복 재생은 06으로 중단합니다. 새 장면을 열기 전에도 06을 실행합니다.
5. 코드 파일을 바꾼 후 모듈 코드가 갱신되지 않으면 앱을 재시작하고 00을 실행합니다.

## CAD 변환

STEP Import는 앱 기본 USD Open과 다릅니다. 강사가 [CAD Converter 설명](https://docs.omniverse.nvidia.com/extensions/latest/ext_cad-converter/manual.html)에 따라 설치된 변환 기능과 라이선스 조건을 확인하고 BX200L STP를 사전 변환합니다. `File > Import` 또는 Content의 `Convert to USD`가 제공될 때 사용합니다.

교육장에 CAD 변환 기능이 없으면 동봉된 `shared/assets/cad/BX200L-C001.usd`로 같은 구조화 실습을 진행합니다. 이 경우 실습 기록에 **기변환 USD 활용**이라고 적습니다. STEP 변환을 수행했다고 기록하지 않습니다.

## Nucleus

Nucleus Workstation과 Launcher는 2025-10-01 폐기되었습니다. 신규 Workstation 설치를 필수 준비로 요구하지 않습니다. [공식 변경 안내](https://developer.nvidia.com/omniverse/legacy-tools)를 참고하세요.

Nucleus 실습은 기관이 제공하는 서버 주소·개인 계정·교육용 경로·읽기/쓰기 권한을 강사가 사전에 확인한 경우 진행합니다. 제공 서버가 없으면 Day 1 Part 6의 로컬 Layer 분업을 실시합니다. 로컬 파일 공유를 Nucleus Live 협업과 동일하다고 설명하지 않습니다.

## 문제 해결

| 증상 | 확인 및 복구 |
|---|---|
| 장비가 없음 | 저장소 전체 위치와 `shared/assets/cad` 확인. 경로 이동 후 전체 다시 열기 |
| 화면이 비어 보임 | `/World/Camera` 선택 또는 `/World` Frame Selection |
| CAD가 너무 큼/작음 | 원본 단위·경계 크기 비교. metersPerUnit 변경만으로 형상이 환산되지는 않음 |
| Cube가 낙하하지 않음 | 03_physics 체크포인트, Play, PhysicsScene 및 RigidBodyEnabled 확인 |
| Cube가 바닥 통과 | Ground의 CollisionAPI, 작업물 CollisionAPI 확인 |
| 상태 색이 안 바뀜 | 장비 원본 재질이 아니라 `/World/StatusLamp` 확인. CSV 및 Console 오류 확인 |
| 비동기 실행이 멈추지 않음 | 06 실행. 작업이 다른 Script Editor 전역에서 실행되었다면 앱 재시작 |
| USD만 열리고 물리 불가 | OpenUSD 파싱 성공과 Isaac Sim 런타임 실행을 구분. 강사 PC 시연 후 관찰 기록 |
