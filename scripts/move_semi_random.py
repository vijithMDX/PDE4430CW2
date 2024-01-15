#!/usr/bin/env python3

import random
import rospy
import time
import tf

from gazebo_msgs.msg import ModelState

rospy.wait_for_service('gazebo/set_model_state')

pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
rospy.init_node('mover', anonymous=True)
time.sleep(1)
message=ModelState()
message.reference_frame="world"

message.model_name = "small_ball"
message.pose.position.x = random.uniform(1.5,-1.5)
message.pose.position.y = random.uniform(-1.4,-1.6)
pub.publish(message)

message.model_name = "medium_ball"
message.pose.position.x = random.uniform(1.5,-1.5)
message.pose.position.y = random.uniform(-.4,-.6)
pub.publish(message)

message.model_name = "large_ball"
message.pose.position.x = random.uniform(1.5,-1.5)
message.pose.position.y = random.uniform(.4,.6)
pub.publish(message)

