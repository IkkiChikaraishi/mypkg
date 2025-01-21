#SPDX-FileCopyrightText:2025 Ikki Chikaraishi
#SPDX-Licence-Identifier:BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

rclpy.init()
node = Node("listener")


def free_cb(msg):
    global node
    node.get_logger().info("Free_Memory: %d" % msg.data)

def total_cb(msg):
    global node
    node.get_logger().info("Total_Memory: %d" % msg.data)

def used_cb(msg):
    global node
    node.get_logger().info("Used_memory: %d" % msg.data)

def main():
    free_pub = node.create_subscription(Int64, "free_memory", free_cb, 10)
    total_pub = node.create_subscription(Int64, "total_memory", total_cb, 10)
    used_pub = node.create_subscription(Int64, "used_memory", used_cb, 10)
    rclpy.spin(node)
