# Ch.Beta · 로봇 관절 기록과 재생

Ch.5의 `5.5.5.4. Publish Joint Commands.sh`를 Python ROS 2 노드로 확장한 예제입니다. **실제 로봇 드라이버가 발행하는 JointState를 받아 기록하고, Isaac Sim의 `/joint_command`로 중계**합니다. 기본 실습에서는 실물 대신 모의 6축 로봇을 사용합니다.

```text
실제 로봇 드라이버 또는 모의 로봇 → JointState ┬→ rosbag 기록
                                             └→ Python 중계 → /joint_command → Isaac Sim
기록된 rosbag → /replay/joint_states → Python 중계 → /joint_command → Isaac Sim
```

| 파일 | 역할 |
|---|---|
| scripts/01_mock_robot.py | joint1~joint6의 합성 관절 상태 발행 |
| scripts/02_record_joint_states.sh | 선택한 상태 토픽을 SQLite3 rosbag으로 기록 |
| scripts/03_joint_state_to_command.py | 이름 대응·값 검사 후 위치 명령 발행 |
| scripts/04_play_joint_states.sh | bag을 별도 재생 토픽으로 발행 |
| config/relay.yaml | 입력/출력 토픽과 관절 이름 대응 |
| scripts/joint_mapping.py | 메시지 검사 및 관절 순서 변환 |

## 실행 환경

ROS 2 Jazzy의 Ubuntu/Linux 터미널용입니다. **Isaac Sim Script Editor에 넣는 코드가 아닙니다.** `rclpy`, `sensor_msgs`, `ros2 bag`, SQLite3 저장 플러그인이 필요합니다. 각 터미널에서 아래를 실행하고 Ch.Beta 폴더로 이동하세요.

```bash
source /opt/ros/jazzy/setup.bash
cd /home/sybae/isaacsim/extsUser/NVIDIA-Omniverse-Books---Practice-Part/Ch.Beta
```

다른 PC에서는 cd 경로를 수정하세요. ROS_DISTRO가 다르면 setup 경로와 `ros2 bag --help` 옵션을 확인합니다. colcon 빌드 없이 시스템 Python으로 실행합니다. Isaac Sim과 터미널은 같은 ROS_DOMAIN_ID 및 서로 통신 가능한 DDS 환경이어야 합니다.

Ch.5와 동일하게 메시지는 `sensor_msgs/msg/JointState`, 관절 이름은 `joint1`~`joint6`입니다. 회전 관절 position은 rad, 직선 관절은 m입니다. 이 예제는 **위치만** 보내며 velocity와 effort는 비웁니다. 실제 로봇 드라이버 설치·접속 코드는 제조사마다 달라 포함하지 않습니다.

## 1. 모의 로봇 상태 만들기

터미널 A:

```bash
python3 scripts/01_mock_robot.py
```

20Hz로 `/demo_robot/joint_states`를 발행합니다. Ch.5의 예시 자세 주변에서 부드럽게 변하는 합성 값입니다. 실제 센서 데이터가 아닙니다.

터미널 B에서 확인:

```bash
ros2 topic echo /demo_robot/joint_states --once
ros2 topic hz /demo_robot/joint_states
```

`hz` 확인을 마치면 Ctrl+C로 종료합니다.

## 2. ROSBAG 기록하기

터미널 B:

```bash
bash scripts/02_record_joint_states.sh /demo_robot/joint_states bag/my_first_motion
```

10초 정도 기록하고 **터미널 B에서 Ctrl+C**를 누릅니다. recorder 종료를 기다린 뒤 확인합니다.

```bash
ros2 bag info bag/my_first_motion
```

`metadata.yaml`과 `.db3` 파일이 생성되고 메시지 개수가 0보다 큰지 확인합니다. 같은 출력 폴더는 덮어쓰지 않습니다. 다시 기록하려면 다른 이름을 지정하세요. bag 폴더는 전체를 함께 복사합니다. 개인 기록은 Git에서 제외됩니다.

## 3. 실시간 상태 → 명령 중계

모의 로봇 A를 실행한 상태에서 터미널 C:

```bash
python3 scripts/03_joint_state_to_command.py --ros-args --params-file config/relay.yaml
```

터미널 D:

```bash
ros2 topic echo /joint_command --once
```

입력 이름 배열의 순서가 바뀌어도 `name`을 기준으로 매핑합니다. 필수 관절 누락, name/position 길이 불일치, 중복 이름, NaN/Inf는 명령을 생략하고 경고를 출력합니다. 새로운 입력을 받을 때만 발행하므로 입력이 멈추면 이전 값을 반복 전송하지 않습니다. 이것은 실물 로봇의 정지 명령이나 watchdog을 대신하지 않습니다.

Isaac Sim에서는 Ch.5에 사용한 로봇과 ROS 2 Subscribe Joint State → Articulation Controller 연결을 준비하고, 구독 토픽을 `/joint_command`로 지정한 뒤 Play합니다. Articulation의 실제 관절 이름이 다르면 아래 매핑을 수정합니다. `echo` 수신 성공과 로봇의 실제 움직임 확인은 별개입니다.

## 4. 기록한 움직임을 다시 보내기

**모의 발행기 A와 기존 중계기 C를 Ctrl+C로 종료**합니다. 명령 토픽에 여러 중계기를 동시에 연결하지 않습니다.

터미널 C에서 재생 입력을 받는 중계기를 시작합니다.

```bash
python3 scripts/03_joint_state_to_command.py --ros-args \
  --params-file config/relay.yaml -p input_topic:=/replay/joint_states
```

터미널 B:

```bash
bash scripts/04_play_joint_states.sh bag/my_first_motion
```

기록한 상태만 `/replay/joint_states`로 remap해서 재생합니다. 원래 실물 상태 토픽에 재생 메시지를 섞지 않습니다. 중계기는 기록 시각 대신 현재 ROS 시각을 명령 stamp에 넣고, 관절 위치를 `/joint_command`로 보냅니다. bag 내부 수신 시각 간격에 따라 재생하며 재생 배율은 header 시각이나 관절값을 바꾸지 않습니다.

절반 속도로 비교:

```bash
bash scripts/04_play_joint_states.sh bag/my_first_motion /demo_robot/joint_states 0.5
```

종료하려면 플레이어와 중계기에서 Ctrl+C를 누릅니다. 무한 반복 재생은 기본 설정에 넣지 않았습니다.

## 5. 실제 로봇 JointState로 바꾸기

실물 로봇의 ROS 드라이버를 먼저 실행하고 **실제 출력 이름과 타입**을 확인합니다.

```bash
ros2 topic list -t
ros2 topic info /실제_상태_토픽 --verbose
ros2 topic echo /실제_상태_토픽 --once
```

`/실제_상태_토픽`은 예시 자리표시자입니다. 실제 메시지가 `sensor_msgs/msg/JointState`이고 여섯 관절의 위치를 포함하는지 확인하세요. 제조사 전용 메시지라면 변환 노드가 먼저 필요합니다.

예를 들어 실제 토픽이 `/robot/joint_states`라면:

```bash
bash scripts/02_record_joint_states.sh /robot/joint_states bag/real_robot_motion

# 기록과 동시에 중계할 때는 별도 터미널에서 실행
python3 scripts/03_joint_state_to_command.py --ros-args \
  --params-file config/relay.yaml -p input_topic:=/robot/joint_states

# 기록 종료 후 재생 중계기를 먼저 실행한 다음:
bash scripts/04_play_joint_states.sh bag/real_robot_motion /robot/joint_states
```

실제 이름이 axis_1~axis_6이면 `config/relay.yaml`의 `source_joint_names`를 수정하고, `target_joint_names`는 Isaac Sim 이름으로 맞춥니다. 같은 인덱스의 source와 target이 연결됩니다. 부호·영점·기어비 변환은 구현하지 않았으므로 두 로봇의 관절 좌표 정의도 일치해야 합니다. 서로 다른 기구의 위치를 단순 대응시키는 예제가 아닙니다.

출력 `/joint_command`는 **Ch.5의 시뮬레이터 명령 인터페이스**입니다. 실물 로봇 컨트롤러가 JointTrajectory나 전용 action을 요구한다면 이 출력으로 직접 제어할 수 없습니다. 이 스크립트에는 실물 구동용 제한 속도·가속도·충돌 검사·비상정지 연동이 없습니다.

## 문제 해결

| 증상 | 확인 |
|---|---|
| Python import 실패 | ROS setup을 실행한 시스템 python3인지 확인 |
| bag 메시지 0개 | 발행기가 실행 중인지, topic 이름·타입·DDS 통신 확인 |
| echo는 되는데 중계 안 됨 | 필수 관절 이름·position 개수와 노드 경고 확인 |
| 모의 상태와 실제 상태 혼합 | 모의 발행기 종료 후 input_topic을 실제 토픽으로 변경 |
| 중계가 두 배로 보임 | `/joint_command` publisher 개수와 실행 중인 중계기 확인 |
| 명령은 수신되지만 로봇 정지 | Sim Play, ROS Bridge, Controller 연결, Articulation 및 joint 이름 확인 |
| 재생은 끝났는데 자세 유지 | 입력 종료는 정지/초기화 명령이 아님. Sim Stop은 별도로 수행 |
| QoS 불일치 | `ros2 topic info --verbose` 확인. 입력은 best-effort/volatile, 출력은 reliable/volatile |

입력은 sensor-data QoS를 사용하므로 실시간 전달 중 일부 샘플 손실은 가능하고, 이 중계기는 모든 샘플의 무손실 전달을 보장하지 않습니다. 고속 기록에서 누락 여부는 rosbag의 기록 수와 발행 조건을 별도로 비교하세요.

## 실습 완료 기준

- bag info의 토픽·메시지 개수를 기록한다.
- 실시간 중계와 bag 재생의 차이를 설명한다.
- 1.0배/0.5배 재생 시 값과 시간 간격의 차이를 관찰한다.
- 실물 데이터인지 합성 데이터인지 표시한다.
- Isaac Sim에서 실제 움직임을 확인했는지, 토픽만 확인했는지 구분한다.

공식 참고: [JointState 정의](https://github.com/ros2/common_interfaces/blob/jazzy/sensor_msgs/msg/JointState.msg), [ROS 2 rosbag2](https://github.com/ros2/rosbag2/tree/jazzy). 이 예제의 CLI 옵션은 설치된 Jazzy의 도움말로도 확인했습니다.

## 다른 자료와 함께 사용할 때

- [직접 bag 재생](Apply_Live.md): Python 중계기 없이 기록된 메시지를 명령 토픽으로 보냅니다. QoS 설정도 함께 사용하세요.
- [Kit-CAE 예제 설명](KIT-CAE.md): 별도 앱과 CAE 샘플 데이터가 필요한 선택 과정입니다.
- [Alpha와의 재사용 범위](../Ch.Alpha/docs/REUSE.md): Alpha의 1축 팔은 Beta 기본 6축 설정과 바로 연결되지 않습니다.

교육생마다 다른 ROS_DOMAIN_ID를 쓰면 같은 네트워크에서 조별 명령이 섞이는 것을 피할 수 있습니다. 각 조의 Isaac Sim과 터미널에는 같은 값을 설정하고, 서로 다른 조에는 다른 값을 지정하세요. 외부 로봇을 연결할 때는 해당 드라이버의 통신 설정에 맞춥니다.
