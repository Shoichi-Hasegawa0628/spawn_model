#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Object file path ##
# PATH = "frontiers2021_gazebo_worlds"
PATH = "tmc_gazebo_worlds"

###################################################
## Object file name
# tableware

# fruits
banana = "ycb_011_banana"
apple = "ycb_013_apple"
orange = "ycb_017_orange"

# bottle
coffee = "nrp_7eleven_bottle_coffee"
muscat = "nrp_7eleven_bottle_juice_grape"
fruits_juice = "nrp_7eleven_bottle_juice_tropical"

# toiletries
cup = "ycb_025_mug"

# snacks
pudding_box = "ycb_008_pudding_box"
chips_bag = "nrp_7eleven_bag_chips_consomme"



###################################################
## Object list
objects = [banana, apple, orange, pudding_box, chips_bag,
           coffee, muscat, fruits_juice, cup]

###################################################
# Target place name, position.
banana_place = [1.187147, -0.196535, 0.400285, -0.004988, -0.008848, -1.435205]
apple_place = [1.224642, 0.144890, 0.400071, 0.026494, 0.026494, -0.032608, 0.001624]
orange_place = [1.207676, 0.505466, 0.400118, 0.004569, 0.013818, 0.000066]
pudding_box_place = [1.169954, 1.160326, 0.627735, 1.560782, 0.486799, -1.720285]
coffee_place = [-0.998882, 0.901094, 0.705108, 0.00, 0.00, 0.00]
fruits_juice_place = [-1.055257, 0.716371, 0.429611, 0.00, 0.00, 0.00]
cup_palce = [-1.036964, -0.145013, 0.400506, -0.001387, -0.004678, -0.000219]
chips_bag_place = [-1.083096, -0.469417, 0.419209, 0.00, 0.00, 0.00]
muscat_place = [-1.106978, -0.734402, 0.405169, 0.00, 0.00, 0.00]

places = [banana_place, apple_place, orange_place, pudding_box_place, chips_bag_place,
          coffee_place, muscat_place, fruits_juice_place, cup_palce]
