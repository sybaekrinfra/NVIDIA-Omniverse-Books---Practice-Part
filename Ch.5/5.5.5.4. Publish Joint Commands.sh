# move the robot to a specific joint configuration
# [0.0, -0.349066, 0.523599, 0.0, 0.785398, 0.0]
ros2 topic pub --once /joint_command sensor_msgs/msg/JointState \
"{
  name: ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6'],
  position: [0.0, -0.349066, 0.523599, 0.0, 0.785398, 0.0],
  velocity: [],
  effort: []
}"

# move the robot to a specific joint configuration
# [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
ros2 topic pub --once /joint_command sensor_msgs/msg/JointState \
"{
  name: ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6'],
  position: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  velocity: [],
  effort: []
}"
