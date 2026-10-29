# PSK 2일차 · 교육생 실습 가이드

목표는 코드를 암기하는 것이 아니라 **어떤 설정을 바꾸면 어떤 결과가 달라지는지 설명하는 것**입니다. 두 사람이 한 조가 되어 조작자와 기록자를 맡고 실습마다 교대하세요. 각 실습의 필수 결과 하나를 완성하면 다음으로 이동합니다. 더 빨리 끝났다면 [추가 미션](PSK_BONUS_MISSIONS.md)을 선택합니다.

## 공통 조작 · 처음 5분

- `Ch.Alpha` 전체를 로컬에 둡니다. File > Open에서 아래 시작 파일을 엽니다.
- Stage에서 Prim(장면 속 물체)을 선택하면 Property에 속성이 나옵니다. 안내된 경로를 Stage 트리에서 펼쳐 찾습니다. 메뉴 이름이 다르면 Property 검색에서 `mass`, `collision`, `target`처럼 속성 이름으로 찾습니다.
- 화면 밖이면 해당 Prim을 선택하고 Frame Selection(F)을 사용합니다. 기본 장면은 `/World/Camera`도 사용할 수 있습니다. 관절 장면은 `/World`를 선택해 F를 누릅니다.
- Play는 실행, Pause는 중간 정지, **Stop은 초기 상태로 복원**입니다. 설정 변경은 Stop 후 합니다.
- 새 장면을 열기 전 진행 중인 스크립트는 `06_stop_tasks.py`로 중단합니다. 작업물을 저장하려면 아래 제출 방법을 사용합니다.
- Script Editor에서 해당 스크립트 전체를 바로 실행합니다. 00 초기화나 공통 모듈 등록은 필요 없습니다.

### 결과 보관

스크린샷에는 선택한 Prim 경로와 변경 값이 보이게 합니다. USD 제출본은 `scripts/13_save_result.py`를 실행합니다. 파일 안의 `FILE_NAME`을 실습별로 바꾸세요. Flatten은 참조 구성을 하나로 합친 제출본이므로 구조 편집 원본과 구별합니다.

`scripts/13_save_result.py`의 `FILE_NAME`을 수정한 뒤 파일 전체를 실행하세요.

스크립트를 쓰지 않는 조는 화면과 기록지로 제출하고 강사가 저장을 돕습니다. 원본 체크포인트에 Save하지 않습니다. 실수로 바꾸었으면 강사의 깨끗한 Ch.Alpha 복사본으로 복구합니다.

## 실습 1 · 장면 검수자 되기 (35분, GUI)

**시작:** `checkpoints/02_structured.usda`. **완료:** 장비·작업물·바닥의 역할과 경로를 기록.

1. `/World`를 펼쳐 Equipment, Workpiece, Ground, StatusLamp를 각각 선택합니다.
2. 장비를 숨겼다 다시 표시합니다. Workpiece까지 함께 사라지는지 관찰합니다. 계층에서 둘이 형제인지 자식인지 설명합니다.
3. Workpiece의 Translate Z를 1.5에서 2.5로 바꿉니다. 장비 형상이 같이 움직이지 않는지 확인합니다.
4. `/World/Equipment`의 Reference가 `shared/assets/cad/BX200L-C001.usd`를 가리키는지 확인합니다. 이는 원본을 복제한 Mesh 편집과 다릅니다.
5. 동료에게 “이 장면에서 움직일 것은 무엇이고, 배경은 무엇인가?”를 설명합니다.

**복구:** 같은 시작 파일을 저장하지 않고 다시 엽니다. 물리 속성이 없는 02에서 아직 낙하하지 않는 것은 정상입니다.

## 실습 2 · 고장 난 크기 찾기 (25분, GUI + 선택 진단)

**시작:** `checkpoints/10_fault_units.usda`. **완료:** 수정 전후 Scale과 원인 한 문장.

1. Equipment를 선택하고 Scale을 기록합니다. Workpiece와 장비의 상대 크기를 비교합니다.
2. Stop 상태에서 Equipment Scale의 X/Y/Z를 모두 **1**로 수정합니다.
3. Frame Selection으로 다시 봅니다. Stage의 `metersPerUnit`만 바꾸는 것과 형상을 실제로 확대·축소하는 것은 다릅니다.
4. 선택: `08_check_readiness.py`를 실행하고 `equipment_height_1_to_3m` 결과를 확인합니다.

**복구:** `03_physics.usda`를 열면 정상 크기와 물리 속성을 가진 기준 장면이 나옵니다. 준비도 검사는 이 수업의 조건 검사이며 SimReady 인증이 아닙니다.

## 실습 3 · 낙하 예측하고 오류 고치기 (40분)

**시작 A:** `06_physics_comparison.usda`. **완료:** 예측·관찰 표와 고친 속성 하나.

1. `/World/Experiment/A`, B, C의 위치와 질량을 확인합니다. A=1kg·1.5m, B=5kg·1.5m, C=1kg·2.5m입니다.
2. 먼저 닿을 순서를 적고 Play → 관찰 → Stop을 두 번 반복합니다. 이 장면에서 같은 높이 A/B는 질량만으로 낙하 시간이 달라지지 않습니다. 화면만으로 정밀 시간을 측정했다고 기록하지 않습니다.
3. **시작 B:** `11_fault_collision.usda`를 열고 Play합니다. 작업물이 바닥을 통과하면 Stop합니다.
4. `/World/Ground`의 `physics:collisionEnabled`를 찾아 True로 켭니다. 다시 Play하여 바닥 접촉을 확인합니다.
5. Collider는 충돌 형상, Rigid Body는 동적 운동, Mass는 질량이라고 서로 설명합니다. Ground는 Collider만 있어도 정적 바닥이 됩니다.

**복구:** 속성을 못 찾으면 08 진단 후 강사에게 Ground를 보여줍니다. `03_physics.usda`가 정상 복구본입니다. 빠른 팀은 [미션 B](PSK_BONUS_MISSIONS.md)를 진행합니다.

## 실습 4 · 한 축만 움직이는 팔 (20분, GUI 또는 숫자 한 개)

**시작:** `12_joint_drive.usda`. **완료:** 목표 각도 0°와 30°의 비교 화면.

1. `/World/Hinge`를 선택합니다. Body1은 Arm, 회전축은 Z, 하한 -60°, 상한 60°인지 확인합니다. Body0이 비어 있는 이 예제는 세계 좌표에 고정됩니다.
2. Drive의 angular target position을 30으로 설정합니다. 찾기 어려우면 `12_joint_target.py`의 `TARGET_DEG = 30`을 실행합니다. Play하여 회전을 관찰합니다.
3. Stop 후 목표를 0으로 바꾸고 다시 Play합니다. Xform 회전값을 직접 바꾸는 것과 물리 Drive로 목표를 주는 것을 구분합니다.
4. 강사가 Arm의 Mass와 Articulation Root를 보여주면 기록합니다. 이 장면의 관성은 충돌 형상·질량을 기반으로 엔진이 계산하며 임의 수치 입력은 하지 않습니다.

**복구:** 원본 장면 재열기. GUI/물리 실행은 교육장 리허설 대상입니다. 움직이지 않으면 강사가 Play, Drive stiffness, Joint body 경로를 확인합니다. BX200L의 실제 관절 모델이 아닙니다.

## 실습 5 · ROS 2 신호를 읽는 운영자 (45분, 강사 연결 시연 + 짝 활동)

**준비:** 강사가 검증한 기존 Ch.4 ROS 2 장면과 실행 환경. 교육생 PC에 ROS 설치를 요구하지 않습니다.

1. 종이에 `시뮬레이터 → joint_states → 외부 프로그램`, `외부 프로그램 → joint_command → 시뮬레이터` 두 흐름을 그립니다.
2. 강사가 터미널에서 `ros2 topic list`, `ros2 topic info /isaac_dofbot/joint_states`, `ros2 topic echo /isaac_dofbot/joint_states --once`를 실행합니다. 실제 topic이 다르면 list에 나온 이름을 사용합니다.
3. 출력의 관절 name과 position을 짝지어 적습니다. position이 모든 관절에서 무조건 각도 단위인 것은 아니며 회전/직선 관절 구분이 필요합니다.
4. 화면에서 관절이 바뀔 때 값이 바뀌는지 관찰합니다. 관측만으로 양방향 제어에 성공했다고 적지 않습니다.
5. 장면 정지·토픽 미발견 상황 중 하나를 강사가 제시하면 “장면 Play → Bridge 활성 → 이름·환경” 순으로 점검할 항목을 고릅니다.

**대체:** 환경 미준비 시 강사의 샘플 메시지로 name/position 대응과 방향 구분만 진행하고 기록지에 `메시지 해석 활동, 실제 연결 미실시`라고 적습니다. 남는 시간에는 실습 7의 배치 활동을 먼저 합니다. 연결 준비는 강사에게 문의하세요.

## 실습 6 · 온도 색상에 속지 않기 (40분)

**시작:** `09_thermal_field.usda`. **완료:** 같은 범례의 두 화면과 출처 표기.

1. `11_thermal_field.py`를 엽니다. `DATASET="thermal_baseline.csv"`로 실행합니다.
2. 온도 범위 30~45°C를 출력에서 확인하고 화면을 저장합니다.
3. DATASET만 `thermal_hotspot.csv`로 바꾸어 실행합니다. 온도 범위 30~95°C를 확인합니다. 범례는 두 경우 모두 20~100°C로 고정합니다.
4. `/World/ThermalPlate`에서 `training:temperature_c`, `training:legend_min_c`, `training:legend_max_c`를 확인합니다. CSV의 face_id는 이 Mesh의 면 번호와 대응합니다.
5. 실제 CAE를 연결하려면 어떤 정보가 더 필요한지 적습니다: 메시/면 대응, 좌표·단위, 시간 단계, 해석 변수와 출처.

**복구:** 장면 재열기 후 11을 실행합니다. 면이 안 보이면 ThermalPlate 선택 후 F. 이 결과는 **교육용 합성 데이터**이며 CAE 해석 결과가 아닙니다.

## 실습 7 · 숫자만 바꾸는 자동화와 이미지 생성 (35분)

**기본 20분:** `07_batch_layout.usda` → `09_batch_layout.py`.

1. ROWS=2, COLUMNS=3으로 실행해 6개를 확인합니다.
2. ROWS=3, COLUMNS=4로 바꿔 12개를 확인합니다. SPACING_M=0.6으로 바꾸면 간격이 달라집니다.
3. 다시 2×3으로 실행해 6개로 돌아오는지 확인합니다. 18개가 누적되는 작업이 아닙니다.
4. 반복 작업을 자동화하고 싶은 업무 하나를 기록합니다. 출력 수와 화면 수가 일치하면 완료입니다.

**Replicator 15분:** 강사가 저장소 `Ch.6/6.5.1. Dataset Creation.py`를 사전 검증한 앱에서 열고 NUM_FRAMES=3인 실행용 사본을 시연합니다. 이 코드는 새 Stage를 여므로 먼저 작업을 저장합니다. 교육생은 RGB·bounding box·semantic segmentation이 각각 무엇을 알려주는지 비교합니다. 출력 위치는 사용자 홈의 `_out_basic_writer_rand`입니다. 완료 메시지 후 파일을 확인합니다.

**대체:** 렌더가 안 되면 기본 배치 실습에서 카메라 구도를 두 개 비교하고, 상자가 겹칠 때 학습용 이미지에 생길 문제를 설명합니다. 이 활동을 데이터셋 생성 성공으로 기록하지 않습니다.

## 마지막 20분 · 팀 결과 공유

1. 실습 2·3·4·6 중 하나를 골라 “변경 전 문제 → 바꾼 속성 → 관찰 결과”를 2분 이내로 설명합니다.
2. 기록지와 화면 2개, 가능한 조는 USD 제출본을 저장합니다.
3. **기본 통과:** 경로/속성 하나를 찾고, 한 변수만 바꾸고, 관찰과 추측을 구분해 설명합니다. 코딩 속도는 평가하지 않습니다.
