#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import rospkg
from gazebo_msgs.srv import DeleteModel
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose, Quaternion
import tf.transformations as tft
from gazebo_ros import gazebo_interface
import random
import glob
from __init__ import *


class SpawnManyModelByDict:
    def __init__(self):
        pass

    def all_delete_model(self):
        rospy.loginfo("All Delete: ")
        for index in range(len(objects)):
            self.delete_model_prox = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
            self.delete_model_prox("training_model_{}".format(index))

    def spawn_model(self, model_name):
        for index, key in enumerate(list(object_place_dict.keys())):
            # 配置する物体を決める
            object_name = key

            # 配置する場所をランダムに決める
            place = object_place_dict[key]

            self.initial_pose = Pose()
            self.initial_pose.position.x = place[0]
            self.initial_pose.position.y = place[1] + (index%3) * 0.175
            self.initial_pose.position.z = place[2]
            roll = place[3]
            pitch = place[4]
            yaw = place[5]
            tmpq = tft.quaternion_from_euler(roll, pitch, yaw)
            q = Quaternion(tmpq[0], tmpq[1], tmpq[2], tmpq[3])
            self.initial_pose.orientation = q

            # Spawn the new model #
            self.model_path = rospkg.RosPack().get_path(PATH) + '/models/{}/'.format(
                objects[index])
            self.model_xml = ''
            rospy.loginfo(model_name)
            rospy.loginfo(self.model_path)
            rospy.loginfo("FILEPATH: " + self.model_path + model_name + '.sdf')
            filename = glob.glob(self.model_path + "/*.sdf")
            print(filename)
            # with open(self.model_path + "*" + '.sdf', 'r') as xml_file:
            with open(filename[0], 'r') as xml_file:
                self.model_xml = xml_file.read().replace('\n', '')
                # model_xml = model_database_template.replace('MODEL_NAME', name)
                gazebo_interface.spawn_sdf_model_client('training_model_{}'.format(index), self.model_xml, "",
                                                        self.initial_pose, "", "/gazebo")
            rospy.loginfo("Spawn_model")


if __name__ == '__main__':
    rospy.init_node('spawn_many_model')
    spawn_many_model = SpawnManyModelByDict()

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
