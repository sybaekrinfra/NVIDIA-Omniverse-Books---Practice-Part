# NVIDIA Omniverse 교재 실습 예제

NVIDIA Omniverse 관련 교재의 실습 예제 코드와 실행 스크립트를 장별로 정리한 저장소입니다.
Isaac Sim, ROS 2, Omniverse Replicator, Isaac Lab을 활용한 예제를 포함합니다.

## 저장소 구성

```
Ch.Alpha/   비개발자 대상 Omniverse 워크숍 및 PSK 2일차 실습
Ch.2/   Kuka 로봇 USD 장면 실습
Ch.3/   BX200L 로봇 CAD 및 USD 변환 실습
Ch.4/   Dofbot 및 Turtiebot 로봇과 ROS 2 연동 실습
Ch.5/   Isaac Sim 센서 및 ROS 2 연동 실습
Ch.6/   Omniverse Replicator를 활용한 합성 데이터셋 생성 실습
Ch.7/   Isaac Lab 설치 및 강화학습(RL) 실습
```

### Ch.Alpha — 실습 중심 워크숍

[워크숍 시작](Ch.Alpha/README.md) · [PSK 강사 운영표](Ch.Alpha/instructor/PSK_DAY2_RUNBOOK.md) · [교육생 실습 가이드](Ch.Alpha/docs/PSK_DAY2_LABS.md)

충북대 워크숍 자료와 복구용 USD 장면을 포함하며, PSK 2일차용 GUI 실습·오류 복구·관절 비교·합성 온도 시각화·추가 미션을 제공합니다.

### Ch.2 — Kuka 로봇 장면

| 파일 | 설명 |
| --- | --- |
| `KukaArm1.usda` | Kuka 로봇 암을 구성한 USD ASCII 장면 파일 |

### Ch.3 — BX200L 로봇 CAD 및 USD

| 파일 | 설명 |
| --- | --- |
| `BX200L-C001.stp` | BX200L 로봇의 STEP 형식 CAD 원본 파일 |
| `BX200L-C001.usd` | BX200L 로봇의 USD 장면 파일 |
| `BX200L-C_F-E.pdf` | BX200L 로봇 CAD 도면 참고 자료 |

### Ch.4 — 로봇 및 ROS 2 연동

| 파일 | 설명 |
| --- | --- |
| `dofbot.usd` | Dofbot 로봇 USD 장면 파일 |
| `turtiebot3.usd` | Turtiebot3 로봇 USD 장면 파일 |
| `dofbot_relay.sh` | `/isaac_dofbot/joint_states` 토픽을 `/dofbot/joint_command`로 중계하는 ROS 2 스크립트 |
| `dofbot_v2/dofbot.usd` | Dofbot v2 로봇 USD 장면 파일 |
| `dofbot_v2/dofbot_ros2.usd` | ROS 2 그래프가 포함된 Dofbot v2 USD 장면 파일 |
| `dofbot_v2/sublayers/` | 로봇 트리, 환경, 재질, 메시, ROS 2 그래프를 분리한 USD 서브레이어 |

### Ch.5 — 센서 및 ROS 2 연동

| 파일 | 설명 |
| --- | --- |
| `5.5.2.2. Camera Publish Rate.py` | 카메라 프림의 `tickRate`(발행 주기)를 설정하는 예제 |
| `5.5.5.4. Publish Joint Commands.sh` | `ros2 topic pub`으로 로봇 조인트 명령(`/joint_command`)을 발행하는 예제 |

### Ch.6 — Replicator 합성 데이터셋 생성

| 파일 | 설명 |
| --- | --- |
| `6.5.1. Dataset Creation.py` | Omniverse Replicator로 RGB, 2D 바운딩 박스, 시맨틱 세그멘테이션을 포함한 합성 데이터셋을 생성하는 예제 |

### Ch.7 — Isaac Lab 설치 및 강화학습

| 파일 | 설명 |
| --- | --- |
| `7.4.1. Prepare uv, Isaac Lab Source.sh` | `uv` 설치 및 Isaac Lab 소스 클론 |
| `7.4.2 Install Python VE, Isaac Lab Pacakge.sh` | Python 가상환경 구성 및 Isaac Lab 패키지 설치 |
| `7.4.3. Task List Check.sh` | 등록된 태스크 목록 확인 |
| `7.4.3. Verify Install - 1, 2.sh` | 설치 검증 스크립트 |
| `7.5.2. Smoke Test.sh` | 설치 상태 스모크 테스트 |
| `7.5.3. Headless.sh` | 헤드리스 모드 실행 |
| `7.5.4. Play Result.sh` | 학습된 정책(policy)을 재생(play)하는 예제 |
| `7.5.5. Evaluate Result.sh` | 학습 결과를 평가하는 예제 |
| `7.7.1. Dofbot Ready.sh` | Dofbot 로봇 환경 준비 |
| `7.7.2. Dofbot RL.sh` | Dofbot 강화학습 훈련 실행 (`rsl_rl`) |

각 장 폴더에는 실습 실행 결과를 확인할 수 있는 스크린샷(`.png`)이 함께 포함되어 있습니다.

## 실행 환경

- **NVIDIA Isaac Sim** / **Isaac Lab**
- **ROS 2** (Ch.4~Ch.5 로봇 연동 및 조인트 명령 예제)
- Python 3.x, `uv` 패키지 매니저 (Ch.7 설치 스크립트 기준)
- CUDA 지원 GPU (RL 학습 실습)

각 스크립트는 교재의 절 번호(예: `7.4.1.`)에 맞춰 파일명이 지정되어 있습니다. 교재 본문의 안내에 따라 순서대로 실행하는 것을 권장합니다.
