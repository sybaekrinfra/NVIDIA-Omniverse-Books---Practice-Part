"""실제/기록된 JointState → Ch.5 Isaac Sim JointState 명령. ROS 터미널용."""
import time
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data, QoSProfile, ReliabilityPolicy
from sensor_msgs.msg import JointState
from joint_mapping import map_positions


class JointStateToCommand(Node):
    def __init__(self):
        super().__init__('joint_state_to_command')
        source = self.declare_parameter('input_topic', '/demo_robot/joint_states').value
        target = self.declare_parameter('output_topic', '/joint_command').value
        defaults = [f'joint{i}' for i in range(1, 7)]
        self.source_names = self.declare_parameter('source_joint_names', defaults).value
        self.target_names = self.declare_parameter('target_joint_names', defaults).value
        if (not self.source_names or len(self.source_names) != len(self.target_names)
                or len(set(self.source_names)) != len(self.source_names)
                or len(set(self.target_names)) != len(self.target_names)
                or any(not x.strip() for x in self.source_names + self.target_names)):
            raise ValueError('원본/대상 관절 이름은 빈 값·중복 없이 같은 개수여야 합니다')
        if self.resolve_topic_name(source) == self.resolve_topic_name(target):
            raise ValueError('입력과 출력 토픽이 같습니다. 중계 루프를 만들 수 없습니다')
        self.publisher = self.create_publisher(
            JointState, target, QoSProfile(depth=1, reliability=ReliabilityPolicy.RELIABLE))
        self.subscription = self.create_subscription(
            JointState, source, self.on_state, qos_profile_sensor_data)
        self.last_warning = -float('inf')
        self.get_logger().info(f'{source} → {target} (위치만 전송, 새 메시지 수신 시에만 발행)')

    def on_state(self, state):
        try:
            positions = map_positions(state.name, state.position, self.source_names)
        except ValueError as error:
            now = time.monotonic()
            if now - self.last_warning >= 2:
                self.get_logger().warning(f'명령 생략: {error}')
                self.last_warning = now
            return
        command = JointState()
        # rosbag의 과거 stamp를 명령에 재사용하지 않습니다.
        command.header.stamp = self.get_clock().now().to_msg()
        command.name = list(self.target_names)
        command.position = positions
        command.velocity = []
        command.effort = []
        self.publisher.publish(command)


def main():
    rclpy.init()
    node = None
    try:
        node = JointStateToCommand()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
