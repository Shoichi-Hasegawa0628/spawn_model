#!/usr/bin/env python
# -*- coding: utf-8 -*-
# gazebo world上に指定した位置に物体を配置するコード (Frontiers2021のシナリオ3)
import random
import sys
import numpy as np
import rospy
import rospkg
from gazebo_msgs.srv import DeleteModel
from gazebo_msgs.srv import SpawnModel
# from std_msgs.msg import Header, Float64, Bool, String, Int16
from geometry_msgs.msg import Pose, Quaternion
import tf.transformations as tft
from gazebo_ros import gazebo_interface
from __init__ import *
import argparse


class SpawnManyModel:
    def __init__(self):
        pass

    def all_delete_model(self):
        rospy.loginfo("All Delete: ")
        for index in range(24):
            self.delete_model_prox = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
            self.delete_model_prox("training_model_{}".format(index))

    def spawn_model(self, model_name):
        for index in range(20):
            # 配置する物体の種類を決める
            o = index

            # 配置する場所を決める
            max_prob = max(prob[o])
            if prob[o].count(max_prob) > 1:
                indexes = [i for i, e in enumerate(prob[o]) if e == max_prob]
                s = random.choice(indexes)

            else:
                s = prob[o].index(max_prob)

            self.initial_pose = Pose()
            self.initial_pose.position.x = places[o][s][0]
            self.initial_pose.position.y = places[o][s][1]
            self.initial_pose.position.z = places[o][s][2]
            roll = places[o][s][3]
            pitch = places[o][s][4]
            yaw = places[o][s][5]
            tmpq = tft.quaternion_from_euler(roll, pitch, yaw)
            q = Quaternion(tmpq[0], tmpq[1], tmpq[2], tmpq[3])
            self.initial_pose.orientation = q

            # Spawn the new model #
            self.model_path = rospkg.RosPack().get_path('frontiers2021_gazebo_worlds') + '/models/{}/'.format(
                objects[o])
            self.model_xml = ''
            rospy.loginfo(model_name)
            rospy.loginfo(self.model_path)
            rospy.loginfo("FILEPATH: " + self.model_path + model_name + '.sdf')
            with open(self.model_path + model_name + '.sdf', 'r') as xml_file:
                self.model_xml = xml_file.read().replace('\n', '')
                # model_xml = model_database_template.replace('MODEL_NAME', name)
                gazebo_interface.spawn_sdf_model_client('training_model_{}'.format(index), self.model_xml, "",
                                                        self.initial_pose, "", "/gazebo")
            rospy.loginfo("Spawn_model")


if __name__ == '__main__':
    rospy.init_node('spawn_many_model')
    spawn_many_model = SpawnManyModel()

    ## spawnかdeleteを入力して、Enterを押すまで待機
    while True:
        get_key = input("Please input word : spawn or delete\n")
        if (get_key == "spawn"):
            print(get_key)
            spawn_many_model.spawn_model("model")
            break
        elif (get_key == "delete"):
            print(get_key)
            spawn_many_model.all_delete_model()
            break
        print("The command is different, please enter the correct command.\n")

