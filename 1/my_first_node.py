#!/usr/bin/env python3
import rclpy  #this is the libeary for ros2 or ros1
from rclpy.node import Node

#make a node by making a object
class Mynode(Node):
    def __init__(self):
        super().__init__("first_node") # Name of the Node
        self.counter = 0
        self.create_timer(1.0, self.timer_callback)


    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter))
        self.counter+=1 

#So here we define the main function.
def main(args=None):
    

    rclpy.init(args=args) #to enable the communication of ros2 


    node = Mynode()

    rclpy.spin(node) # we use spin to reamining the execution of the node
    

    rclpy.shutdown() #to turn off the communication


#here if we enter main in the command line, the main function will run.
if __name__ == "__main__":
    main()