"""실물 로봇 없이 테스트하는 6축 JointState 발행기. ROS 터미널에서 실행."""
import math
import time
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import JointState


class MockRobot(Node):
    def __init__(self):
        super().__init__('mock_robot')
        topic = self.declare_parameter('topic', '/demo_robot/joint_states').value
        hz = self.declare_parameter('rate_hz', 20.0).value
        if not math.isfinite(hz) or not 0 < hz <= 200:
            raise ValueError('rate_hz는 0 초과 200 이하')
        self.publisher = self.create_publisher(JointState, topic, qos_profile_sensor_data)
        self.started = time.monotonic()
        self.timer = self.create_timer(1.0 / hz, self.publish_state)
        self.get_logger().info(f'교육용 합성 관절 상태 → {topic}')

    def publish_state(self):
        t = time.monotonic() - self.started
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [f'joint{i}' for i in range(1, 7)]
        base = [0.0, -0.349066, 0.523599, 0.0, 0.785398, 0.0]
        msg.position = [value + 0.1 * math.sin(t * 0.5 + i * 0.2)
                        for i, value in enumerate(base)]
        # 이 예제는 위치만 사용합니다. 속도/토크를 계산한 것처럼 채우지 않습니다.
        self.publisher.publish(msg)


def main():
    rclpy.init()
    node = None
    try:
        node = MockRobot()
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
