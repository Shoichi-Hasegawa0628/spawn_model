#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Object file path ##
# PATH = "frontiers2021_gazebo_worlds"
PATH = "tmc_gazebo_worlds"

###################################################
## Object file name

apple = "ycb_013_apple"
# orange = "ycb_017_orange"
master_chef = "ycb_002_master_chef_can"
rubiks_cube = 'ycb_077_rubiks_cube'



banana = 'ycb_011_banana'
pudding_box = "ycb_008_pudding_box"
tomato_soup_can = 'ycb_005_tomato_soup_can'


tennis_ball = 'ycb_056_tennis_ball'
potted_meat_can = 'ycb_010_potted_meat_can'
cup = "ycb_025_mug"




###################################################
## Object list
objects = [rubiks_cube, apple, master_chef, pudding_box, banana, tomato_soup_can, cup, tennis_ball, potted_meat_can]

###################################################
# Target place name, position.
# banana_place = [1.187147, -0.196535, 0.400285, -0.004988, -0.008848, -1.435205]
# apple_place = [1.224642, 0.144890, 0.400071, 0.026494, 0.026494, -0.032608, 0.001624]
# orange_place = [1.207676, 0.505466, 0.400118, 0.004569, 0.013818, 0.000066]
# pudding_box_place = [1.169954, 1.160326, 0.627735, 1.547478, 0.459527, -1.615486]
# cup_palce = [-1.036964, -0.145013, 0.400506, -0.001387, -0.004678, -0.000219]
# rubiks_cube_place = [-1.078609, 0.693531, 0.420312, -0.002509, -0.005559, 0.000435]
# tennis_ball_place = [-1.120329, -0.689464, 0.403392, -0.015839, -0.000793, 0.001960]
# potted_meat_can_place = [-1.082676, -0.356630, 0.407281, 0.030775, -0.005525, 1.537958]

place1 = [1.187147, -0.196535, 0.400285, -0.004988, -0.008848, -1.435205]
place2 = [1.110886, 1.009600, 0.627735, 0.00, 0.00, -1.559631]
place3 = [-1.082676, -0.684636, 0.407281, 0.030775, -0.005525, 1.537958]

object_place_dict = {"ycb_013_apple": place1, "ycb_002_master_chef_can": place1, 'ycb_077_rubiks_cube':place1,
                     "ycb_008_pudding_box": place2, "ycb_011_banana": place2, 'ycb_005_tomato_soup_can': place2,
                     'ycb_056_tennis_ball': place3, 'ycb_010_potted_meat_can': place3, "ycb_025_mug": place3}

# places = [banana_place, apple_place, orange_place, pudding_box_place, cup_palce,
#           rubiks_cube_place, tennis_ball_place, potted_meat_can_place]
