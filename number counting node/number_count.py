#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumbercountNode(Node): 
    def __init__(self):
        self.total = 0 # Total Sum to publish in number count topic
        self.flag = 0  # To check the subscribe number is varey from the 1st one
        super().__init__("number_count") 
        self.subscriber_=self.create_subscription(Int64,"number",self.count,10)

        self.publisher__=self.create_publisher(Int64,"number_count",10)

        self.get_logger().info("number count node is working.")
    
    def count(self,msg):
        if (self.flag == int(msg.data)):
            pass
        else:
            self.total +=1
            self.flag = int(msg.data)

            msg.data = self.total
            self.publisher__.publish(msg)

            self.get_logger().info(str(msg.data)) # get logger only strings types are allowed





def main(args=None):
    rclpy.init(args=args)
    node = NumbercountNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()