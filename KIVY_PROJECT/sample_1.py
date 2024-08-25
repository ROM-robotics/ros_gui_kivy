#!/usr/bin/env python

#import rclpy
#from rclcpy.node import Node
from kivymd import MDApp
from kivy.lang import Builder

class TutorialApp1(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.screen = Builder.load_file('/home/mr_robot/gui_ws/src/kivy_tuto/gui.kv')

	def build(self):
		return self.screen








def main(args=None):
	pass





if __name__ == '__main__':
	main()
	TutorialApp1.run()
