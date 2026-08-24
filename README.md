# NVIDIA Omniverse Books - Practice Part

NVIDIA Omniverse 관련 교재의 실습(Practice) 예제 코드와 스크립트를 챕터별로 정리한 저장소입니다.

## 구성

```
Ch.5/   Isaac Sim 센서 및 ROS 2 연동 실습
Ch.6/   Replicator를 활용한 합성 데이터셋 생성 실습
Ch.7/   Isaac Lab 설치 및 강화학습(RL) 실습
```

### Ch.5 — 센서 & ROS 2

| 파일 | 설명 |
| --- | --- |
| `5.5.2.2. Camera Publish Rate.py` | 카메라 프림의 `tickRate`(퍼블리시 주기)를 설정하는 예제 |
| `5.5.5.4. Publish Joint Commands.sh` | `ros2 topic pub`으로 로봇 조인트 명령(`/joint_command`)을 퍼블리시하는 예제 |

### Ch.6 — Replicator 데이터셋 생성

| 파일 | 설명 |
| --- | --- |
| `6.5.1. Dataset Creation.py` | Omni Replicator로 RGB, 2D Bounding Box, Semantic Segmentation을 포함한 합성 데이터셋을 생성하는 예제 |

### Ch.7 — Isaac Lab 설치 및 RL 학습

| 파일 | 설명 |
| --- | --- |
| `7.4.1. Prepare uv, Isaac Lab Source.sh` | `uv` 설치 및 Isaac Lab 소스 클론 |
| `7.4.2 Install Python VE, Isaac Lab Pacakge.sh` | Python 가상환경 구성 및 Isaac Lab 패키지 설치 |
| `7.4.3. Task List Check.sh` | 등록된 태스크 목록 확인 |
| `7.4.3. Verify Install - 1, 2.sh` | 설치 검증 스크립트 |
| `7.5.2. Smoke Test.sh` | 설치 상태 스모크 테스트 |
| `7.5.3. Headless.sh` | 헤드리스 모드 실행 |
| `7.5.4. Play Result.sh` | 학습된 정책(policy) 재생(play) |
| `7.5.5. Evaluate Result.sh` | 학습 결과 평가 |
| `7.7.1. Dofbot Ready.sh` | Dofbot 로봇 환경 준비 |
| `7.7.2. Dofbot RL.sh` | Dofbot 강화학습 훈련 실행 (`rsl_rl`) |

각 챕터 폴더에는 실습 실행 결과를 확인할 수 있는 스크린샷(`.png`)이 함께 포함되어 있습니다.

## 실행 환경

- **NVIDIA Isaac Sim** / **Isaac Lab**
- **ROS 2** (Ch.5 조인트 명령 예제)
- Python 3.x, `uv` 패키지 매니저 (Ch.7 설치 스크립트 기준)
- CUDA 지원 GPU (RL 학습 실습)

각 스크립트는 교재의 절 번호(예: `7.4.1.`)에 맞춰 파일명이 지정되어 있으며, 교재 본문의 안내와 함께 순서대로 실행하는 것을 권장합니다.
