#! /usr/bin/env python3

import rospy
import actionlib
from action2_pkg.msg import demoAction,demoFeedback,demoResult,demoGoal


def feedback_callback(feedback):
    print("objetivo: " + str(feedback.current_number))


def nav_client(user_coords):
    client = actionlib.SimpleActionClient("demo_as", demoAction)

    client.wait_for_server()

    point_msg = user_coords

    goal = demoGoal(point_msg)

    client.send_goal(goal, feedback_cb=feedback_callback)

    client.wait_for_result()

    return client.get_result()


if __name__ == "__main__":
    try:
        rospy.init_node("action_client_node")

        objetivo = input("cual es el objetivo ")
        objetivo = int(objetivo)

        result = nav_client(objetivo)
        

    except rospy.ROSInterruptException:
        print("Program interrupted")