#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from moveit import MoveItPy

from moveit.core.robot_state import RobotState
from tf_transformations import quaternion_from_euler

class MoveItPoseController(Node):
    def __init__(self):
        super().__init__('moveit_pose_controller')
        
        # Initialize MoveItPy
        self.moveit = MoveItPy(node_name="moveit_py")
        self.arm = self.moveit.get_planning_component("ur_manipulator")
        
        # Set reference frame and end effector
        self.arm.set_pose_reference_frame("base_link")  # Change if needed
        self.arm.set_end_effector("tool0")  # Verify your URDF's EE link name

    def move_to_pose(self, position, orientation=None):
        """
        Move to specified pose
        :param position: [x, y, z] in meters
        :param orientation: [roll, pitch, yaw] in radians (optional)
        """
        # Create Pose message
        pose = Pose()
        pose.position.x = position[0]
        pose.position.y = position[1]
        pose.position.z = position[2]
        
        # Set orientation (default to upright if not specified)
        if orientation is None:
            orientation = [0.0, 1.57, 0.0]  # Default: facing downward (adjust as needed)
            
        q = quaternion_from_euler(*orientation)
        pose.orientation.x = q[0]
        pose.orientation.y = q[1]
        pose.orientation.z = q[2]
        pose.orientation.w = q[3]

        # Set pose goal
        self.arm.set_pose_goal(pose)
        
        # Plan and execute
        plan_result = self.arm.plan()
        if plan_result:
            self.get_logger().info("Executing pose plan...")
            self.arm.execute()
        else:
            self.get_logger().error("Pose planning failed!")

def main(args=None):
    rclpy.init(args=args)
    controller = MoveItPoseController()
    
    # Example: Move to position [0.4, 0.1, 0.4] with default orientation
    controller.move_to_pose(position=[0.4, 0.1, 0.4])
    
    # Example: Specify custom orientation (roll=0, pitch=0, yaw=0)
    # controller.move_to_pose(position=[0.4, 0.1, 0.4], orientation=[0.0, 0.0, 0.0])
    
    rclpy.spin(controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
