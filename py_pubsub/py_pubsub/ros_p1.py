#!/usr/bin/env python

import rclpy
from rclcpy.node import Node
from std_msgs.msg import String

from kivymd import MDApp
from kivy.lang import Builder

class MyROS2Node(Node):
    def __init__(self):
        super().__init__('my_ros2_node')
        # Set up ROS 2 publisher, subscriber, etc.
		
class TutorialApp1(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.screen = Builder.load_file('/home/mr_robot/kivy_ws/src/ros_gui_kivy/py_pubsub/gui.kv')

	def build(self):
		return self.screen
	

    def start_ros2(self):
        # Initialize and start ROS 2 node
        rclpy.init()
        self.node = MyROS2Node()
        rclpy.spin(self.node)
        rclpy.shutdown()


if __name__ == '__main__':
	TutorialApp1.run()
