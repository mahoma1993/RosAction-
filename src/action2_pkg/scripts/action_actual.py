#! /usr/bin/env python3

import rospy
from  std_msgs.msg import Int32

def robot_point_pub(user_coords):

    pub = rospy.Publisher("contador_inicial", Int32, queue_size=10)
    print("Publishing...")

    rate = rospy.Rate(40)

    while not rospy.is_shutdown():
        pub.publish(Int32(user_coords))
        rate.sleep()



if __name__ == "__main__":
    try:
        rospy.init_node("robot_point_pub_node")

        user_x = input("la posicion actual: ")
        

        user_coords = (int(user_x))

        robot_point_pub(user_coords)

    except rospy.ROSInterruptException:
        print("Exception Occured")