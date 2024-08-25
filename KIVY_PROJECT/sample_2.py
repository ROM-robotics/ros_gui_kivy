import rclpy
from rclpy.node import Node
from kivy.lang import Builder
from kivymd.app import MDApp

class MyROS2Node(Node):
    def __init__(self):
        super().__init__('my_ros2_node')
        # Set up ROS 2 publisher, subscriber, etc.

class MyApp(MDApp):
    def build(self):
        # Load the KV design file for KivyMD UI
        return Builder.load_string('''
        MDBoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: "ROS 2 and KivyMD Integration"
                halign: 'center'
            MDRaisedButton:
                text: "Start ROS 2 Node"
                on_press: app.start_ros2()
        ''')

    def start_ros2(self):
        # Initialize and start ROS 2 node
        rclpy.init()
        self.node = MyROS2Node()
        rclpy.spin(self.node)
        rclpy.shutdown()

if __name__ == '__main__':
    MyApp().run()
