# Isaac Sim 관절 상태를 기록하고 바로 재생하기

Isaac Sim이 발행하는 `/demo_robot/joint_states`를 rosbag에 저장하고, 저장한 메시지를 명령 토픽으로 직접 재생합니다. 이 방식은 `01_mock_robot.py`와 Python 중계기가 필요하지 않습니다.

## 준비

- Isaac Sim의 ROS 2 Bridge를 활성화하고 Play합니다.
- 상태 발행 토픽은 `/demo_robot/joint_states`, 메시지 타입은 `sensor_msgs/msg/JointState`로 설정합니다.
- 명령 구독 토픽도 `sensor_msgs/msg/JointState`를 사용하고 Articulation Controller에 연결합니다.
- 기록된 관절 이름과 시뮬레이터의 관절 이름이 일치해야 합니다.
- 각 터미널에서 ROS 환경을 활성화하고 Ch.Beta 폴더로 이동합니다. Isaac Sim과 같은 ROS_DOMAIN_ID를 사용합니다.

```bash
source /opt/ros/jazzy/setup.bash
cd /home/sybae/isaacsim/extsUser/NVIDIA-Omniverse-Books---Practice-Part/Ch.Beta
```

다른 PC에서는 위 경로를 수정하세요. 발행 상태를 먼저 확인합니다.

```bash
ros2 topic echo /demo_robot/joint_states --once
```

## 1. 움직임 기록

```bash
bash scripts/02_record_joint_states.sh \
  /demo_robot/joint_states bag/my_first_motion
```

Isaac Sim에서 로봇을 움직입니다. 기록이 끝나면 **기록 터미널에서 Ctrl+C**를 누르고 recorder 종료를 기다립니다.

```bash
ros2 bag info bag/my_first_motion
```

토픽 이름과 메시지 개수가 정상인지 확인합니다. 같은 bag 폴더는 덮어쓰지 않으므로 다시 기록할 때는 새 이름을 지정하세요.

## 2. 저장한 상태를 명령으로 직접 재생

기록할 때 사용한 제어기와 다른 명령 발행기·Python 중계기를 종료합니다. Isaac Sim은 Play 상태로 유지하고, 아래 두 명령 중 **실제 구독 토픽에 맞는 하나만** 실행하세요.

Isaac Sim이 `/joint_command`를 구독하는 경우:

```bash
ros2 bag play bag/my_first_motion \
  --qos-profile-overrides-path config/direct_play_qos.yaml \
  --topics /demo_robot/joint_states \
  --remap /demo_robot/joint_states:=/joint_command
```

Isaac Sim이 `/demo_robot/joint_command`를 구독하는 경우:

```bash
ros2 bag play bag/my_first_motion \
  --qos-profile-overrides-path config/direct_play_qos.yaml \
  --topics /demo_robot/joint_states \
  --remap /demo_robot/joint_states:=/demo_robot/joint_command
```

`--topics`에는 **bag에 기록된 원래 토픽 이름**을 지정합니다. `--remap`의 왼쪽은 기록된 토픽, 오른쪽은 Isaac Sim이 구독하는 명령 토픽입니다.

```text
bag의 /demo_robot/joint_states → /joint_command → Isaac Sim
```

직접 재생은 `config/direct_play_qos.yaml`로 reliable 발행을 지정하여 reliable 명령 구독기에도 전달되도록 합니다. YAML의 키는 **remap 전 기록 토픽**입니다. 다른 토픽을 기록했다면 YAML의 `/demo_robot/joint_states`도 그 이름으로 바꾸세요.

절반 속도로 재생하려면 위 명령에 `--rate 0.5`를 추가합니다. 중간에 종료하려면 재생 터미널에서 Ctrl+C를 누릅니다. 재생 종료는 로봇 초기화나 정지 명령을 뜻하지 않으며, 시뮬레이션 정지는 Isaac Sim의 Stop으로 수행합니다.

## 직접 재생과 중계 방식의 차이

직접 재생은 기록된 메시지의 토픽 이름만 바꿉니다. 관절 이름·위치·기록 당시 header 시각을 그대로 보내며, **velocity와 effort가 기록되어 있으면 함께 전달**됩니다. 위치만 제어하려면 Isaac Sim Controller의 연결을 확인하세요.

관절 이름 변환, 값 검사, 위치만 전송하거나 현재 시각으로 stamp를 바꾸는 처리가 필요하면 [기존 중계 방식](START_HERE.md)의 `03_joint_state_to_command.py`를 사용합니다.

`04_play_joint_states.sh`는 `/replay/joint_states`로 보내는 중계 방식용입니다. 이 문서의 직접 재생에서는 위의 `ros2 bag play` 명령을 사용하세요.

이 절차의 명령 대상은 Isaac Sim입니다. 실물 로봇 컨트롤러의 구동 인터페이스와 안전 기능을 구현한 예제가 아닙니다.
