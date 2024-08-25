#!/usr/bin/env python

#import rospy
from kivymd import MDApp
from kivy.lang import Builder

class TutorialApp1(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.screen = Builder.load_file('/home/mr_robot/kivy_ws/src/ros_gui_kivy/py_pubsub/gui.kv')

	def build(self):
		return self.screen


if __name__ == '__main__':
	rospy.init_node('simple_gup', anonymous=True)
	TutorialApp1.run()
