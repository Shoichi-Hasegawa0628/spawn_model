#!/usr/bin/env python
# -*- coding: utf-8 -*-
# gazebo world上に指定した位置に物体を配置するコード

import sys
import rospy
import rospkg
from gazebo_msgs.srv import DeleteModel
from gazebo_msgs.srv import SpawnModel
#from std_msgs.msg import Header, Float64, Bool, String, Int16
from geometry_msgs.msg import Pose
import argparse

class ActorModel:
    # @staticmethod
    def __init__(self):
        pass

    def delete_model(self, model_name):
        rospy.loginfo("Delete_model: " + model_name)
        # Delete the old model if it's stil around
        self.delete_model_prox = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
        self.delete_model_prox(model_name)
        rospy.loginfo("Delete_model")

    # @staticmethod
    def spawn_model(self, model_name):
        rospy.loginfo("Spawn_model: " + model_name)
        # bedroom, pig_doll
        self.initial_pose = Pose()
        self.initial_pose.position.x = -3.0
        self.initial_pose.position.y = -1.6
        self.initial_pose.position.z = 0.0

        # Spawn the new model #
        self.model_path = rospkg.RosPack().get_path('nrp_gazebo_worlds')+'/models/3rd_generic_toy_doll_pig/'
        self.model_xml = ''
        rospy.loginfo(model_name)
        rospy.loginfo(self.model_path)
        rospy.loginfo("FILEPATH: " + self.model_path + model_name + '.sdf')
        with open (self.model_path + model_name + '.sdf', 'r') as xml_file:
            self.model_xml = xml_file.read().replace('\n', '')
        self.spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        self.spawn_model_prox('training_model', self.model_xml, '', self.initial_pose, 'world')
        rospy.loginfo("Spawn_model")


if __name__ == '__main__':
    rospy.init_node('spawn_model')

    actor_model = ActorModel()
    #rospy.logwarn("Customer entering the environment")
    #human_action = sys.argv[1]
    actor_model.spawn_model("model")
