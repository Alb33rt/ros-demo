#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TutorialNode(Node):
    def __init__(self):
        super().__init__('tutorial_node')
        self.publisher = self.create_publisher(String, 'tutorial_topic', 10)
        self.subscription = self.create_subscription(
            String,
            'tutorial_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello ROS 2 Tutorial! Message #{self.count}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count += 1

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = TutorialNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
