#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberpublisherNode(Node): 
    def __init__(self):
        super().__init__("number_publisher") 

        self.publisher_ = self.create_publisher(Int64,"number",10) #want to add massage type
        self.timer_ = self.create_timer(0.5,self.number_publish) # for every 0.5 time, it runs publish_news node.


        self.get_logger().info("number is publishing. ")  #in logger can only put STRINGS

    def number_publish(self):
        msg=Int64()


        msg.data = 10  # put the input number as needed.


        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberpublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()