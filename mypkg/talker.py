import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0 #カウント用変数


def cb():
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    n += 1


def main():
    node.create_timer(0.5, cb) #タイマー設定
    rclpy.spin(node) #実行（無限ループ）