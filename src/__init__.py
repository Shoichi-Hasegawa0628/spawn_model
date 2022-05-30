#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Object file path ##
PATH = "frontiers2021_gazebo_worlds"

###################################################
## Object file name
# tableware
plate = "ycb_029_plate"
bowl = "ir_bowl"
pitcher_base = "ycb_019_pitcher_base"

# fruits
banana = "ycb_011_banana"
apple = "ycb_013_apple"
orange = "ycb_017_orange"

# snack
cracker_box = "ycb_003_cracker_box"
pudding_box = "ycb_008_pudding_box"
chips_bag = "nrp_7eleven_bag_chips_consomme"

# bottle
coffee = "nrp_7eleven_bottle_coffee"
muscat = "nrp_7eleven_bottle_juice_grape"
fruits_juice = "nrp_7eleven_bottle_juice_tropical"

# doll
penguin_doll = "3rd_generic_toy_doll_penguin"
sheep_doll = "3rd_generic_toy_doll_sheep"
pig_doll = "3rd_generic_toy_doll_pig"

# vehicle_toy
airplane_toy = "ycb_072-a_toy_airplane"
car_toy = "ycb_073-g_lego_duplo"
truck_toy = "ir_truck"

# toiletries
tooth_paste = "ir_tooth_paste"
towel = "ir_towel"
cup = "ir_cup"

# bath_goods
treatments = "ir_treatments"
body_sponge = "ycb_026_sponge"
bath_slipper = "ir_bath_slipper"

###################################################
## Object list
objects = [plate, bowl, pitcher_base, banana, apple,
           orange, cracker_box, pudding_box, chips_bag,
           coffee, muscat, fruits_juice, penguin_doll,
           sheep_doll, pig_doll, airplane_toy, car_toy,
           truck_toy, tooth_paste, towel, cup,
           treatments, body_sponge, bath_slipper]

###################################################
# Target place name, position.
living = [-0.114105, -0.078607, 3.0, -0.000759, 0.000129, 0.133706]
kitchen = [0.875938, -2.357945, 3.0, -0.000760, -0.000233, -0.296452]
bedroom = [-2.760358, -0.389499, 3.0, -0.000128, -0.000918, -1.496207]
bathroom = [-1.062587, 3.753711, 3.0, 0.000826, -0.000479, -2.729761]
places = [living, kitchen, bedroom, bathroom]
