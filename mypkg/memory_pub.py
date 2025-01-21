import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
import psutil

rclpy.init()
node = Node("memory_pub")
free_pub = node.create_publisher(Int64, "free_memory", 10)
used_pub = node.create_publisher(Int64, "used_memory", 10)
total_pub = node.create_publisher(Int64, "total_memory", 10)

def cb():
    global n
    free_msg = Int64()
    used_msg = Int64()
    total_msg = Int64()

    memory_data = psutil.virtual_memory()
    free_msg.data = int(memory_data.free)
    used_msg.data = int(memory_data.used)
    total_msg.data = int(memory_data.total)
    
    free_pub.publish(free_msg)
    used_pub.publish(used_msg)
    total_pub.publish(total_msg)


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
