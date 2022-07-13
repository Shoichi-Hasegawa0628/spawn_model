#!/usr/bin/env python
# -*- coding: utf-8 -*-

## 物体の種類のPATH
# Tableware
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

objects = [plate, bowl, pitcher_base, banana, apple, orange, cracker_box, pudding_box, chips_bag, coffee, muscat,
           fruits_juice, penguin_doll, sheep_doll, pig_doll, airplane_toy, car_toy, truck_toy, tooth_paste, towel, cup,
           treatments, body_sponge, bath_slipper]
###############################################
# target place
living_target = [-0.114105, -0.078607, 3.0, -0.000759, 0.000129, 0.133706]
kitchen_target = [0.875938, -2.357945, 3.0, -0.000760, -0.000233, -0.296452]
bedroom_target = [-2.760358, -0.389499, 3.0, -0.000128, -0.000918, -1.496207]
bathroom_target = [-1.062587, 3.753711, 3.0, 0.000826, -0.000479, -2.729761]
places_target = [living_target, kitchen_target, bedroom_target, bathroom_target]

###############################################
## 物体の位置の座標 (plate)
living_0 = [1.164525, 0.137704, 0.007373, -0.001114, -0.000913, -0.008544]
kitchen_0 = [2.385516, -2.812857, 0.009724, -0.001167, -0.001266, -0.010577]
bedroom_0 = [-2.665412, -1.791184, 0.008915, -0.001226, -0.001202, 0.022525]
bathroom_0 = [-2.350898, 3.385686, 0.004790, -0.001289, -0.001313, -0.004057]
places_0 = [living_0, kitchen_0, bedroom_0, bathroom_0]
prob_0 = [0.2, 0.6, 0.1, 0.1]

## 物体の位置の座標 (bowl)
living_1 = [1.634624, 0.472970, 0.003646, -0.002444, 0.012254, -0.000059]
kitchen_1 = [2.262271, -3.095017, 0.726484, -0.002673, 0.011874, 0.000130]
bedroom_1 = [-3.180006, -1.616874, 0.005476, -0.001792, 0.006032, 0.000001]
bathroom_1 = [-2.474306, 2.877169, 0.001793, -0.000199, 0.011588, -0.000089]
places_1 = [living_1, kitchen_1, bedroom_1, bathroom_1]
prob_1 = [0.2, 0.6, 0.1, 0.1]

## 物体の位置の座標 (pitcher_base)
living_2 = [1.927333, -0.022218, 0.000556, 0.005470, 0.000012, 0.002154]
kitchen_2 = [2.544503, -2.479171, 0.000556, 0.005466, 0.000009, -0.009970]
bedroom_2 = [-1.880411, -2.024284, 0.000558, 0.005420, 0.000004, 0.000568]
bathroom_2 = [-2.717753, 3.653427, 0.002029, 0.004650, -0.000013, -0.004690]
places_2 = [living_2, kitchen_2, bedroom_2, bathroom_2]
prob_2 = [0.2, 0.6, 0.1, 0.1]

## 物体の位置の座標 (banana)
living_3 = [1.381317, -0.046776, 0.004699, -0.004055, -0.007548, 2.508293]
kitchen_3 = [2.263464, -2.717581, 0.006826, -0.005217, -0.007414, 0.859461]
bedroom_3 = [-2.556057, -1.606389, 0.005937, -0.005423, -0.007920, 0.073659]
bathroom_3 = [-2.283055, 3.099283, 0.002192, -0.005381, -0.007735, 0.545148]
places_3 = [living_3, kitchen_3, bedroom_3, bathroom_3]
prob_3 = [0.2, 0.6, 0.1, 0.1]

## 物体の位置の座標 (apple)
living_4 = [1.414119, -0.204653, 0.004363, -0.005482, 0.007519, 0.003861]
kitchen_4 = [2.067206, -2.562400, 0.006241, -0.005415, 0.007434, 0.000704]
bedroom_4 = [-2.673210, -1.573836, 0.005713, 0.025750, -0.032579, 0.001467]
bathroom_4 = [-2.156926, 3.339532, 0.001541, -0.005485, 0.007569, 0.007037]
places_4 = [living_4, kitchen_4, bedroom_4, bathroom_4]
prob_4 = [0.2, 0.6, 0.1, 0.1]

## 物体の位置の座標 (orange)
living_5 = [1.424479, -0.318937, 0.004754, 0.003778, 0.013833, 0.019119]
kitchen_5 = [2.035315, -2.650854, 0.006611, 0.003778, 0.013845, 0.034587]
bedroom_5 = [-2.771722, -1.566790, 0.005747, 0.003769, 0.013815, 0.001886]
bathroom_5 = [-2.121868, 3.224579, 0.002200, 0.031181, 0.054404, -0.024291]
places_5 = [living_5, kitchen_5, bedroom_5, bathroom_5]
prob_5 = [0.2, 0.6, 0.1, 0.1]

## 物体の位置の座標 (cracker_box)
living_6 = [1.912231, 0.261953, 0.002966, 0.000119, 0.011331, -3.082444]
kitchen_6 = [2.603641, -2.676298, 0.009517, 0.001096, 0.008752, 3.127043]
bedroom_6 = [-2.134486, -2.004869, 0.008955, 0.000177, 0.011313, 1.575613]
bathroom_6 = [-2.676280, 2.875980, 0.005197, 0.001230, 0.007406, -0.013054]
places_6 = [living_6, kitchen_6, bedroom_6, bathroom_6]
prob_6 = [30 / 55, 10 / 55, 10 / 55, 5 / 55]

## 物体の位置の座標 (pudding_box)
living_7 = [1.446092, 0.122486, -0.000817, -0.013410, 0.011826, 0.263657]
kitchen_7 = [2.064617, -2.423103, 0.006711, -0.008795, -0.004465, 0.072899]
bedroom_7 = [-2.271606, -1.614792, 0.001112, -0.000121, 0.026897, 0.018504]
bathroom_7 = [-2.300060, 2.814558, -0.007984, -0.008810, -0.004588, 0.020567]
places_7 = [living_7, kitchen_7, bedroom_7, bathroom_7]
prob_7 = [30 / 55, 10 / 55, 10 / 55, 5 / 55]

## 物体の位置の座標 (chips_bag)
living_8 = [1.918906, 0.545559, 0, 0, 0, 0]
kitchen_8 = [2.717570, -2.773090, 0, 0, 0, 0]
bedroom_8 = [-2.376330, -2.005837, 0, 0, 0, -1.602367]
bathroom_8 = [-2.426899, 2.466089, 0, 0, 0, 0]
places_8 = [living_8, kitchen_8, bedroom_8, bathroom_8]
prob_8 = [30 / 55, 10 / 55, 10 / 55, 5 / 55]

## 物体の位置の座標 (coffee)
living_9 = [1.408085, 0.614576, 0, 0, 0, 0]
kitchen_9 = [2.330750, -2.226920, 0, 0, 0, 0]
bedroom_9 = [-2.213642, -1.785904, 0, 0, 0, 1.574171]
bathroom_9 = [-2.372278, 2.986810, 0, 0, 0, 0]
places_9 = [living_9, kitchen_9, bedroom_9, bathroom_9]
prob_9 = [30 / 55, 10 / 55, 10 / 55, 5 / 55]

## 物体の位置の座標 (muscat)
living_10 = [1.389934, 0.478398, 0, 0, 0, 0]
kitchen_10 = [2.201000, -2.144310, 0, 0, 0, 0]
bedroom_10 = [-2.314854, -1.791966, 0, 0, 0, 1.660799]
bathroom_10 = [-2.413729, 3.092382, 0, 0, 0, 0]
places_10 = [living_10, kitchen_10, bedroom_10, bathroom_10]
prob_10 = [30 / 55, 10 / 55, 10 / 55, 5 / 55]

## 物体の位置の座標 (fruits_juice)
living_11 = [1.411788, 0.336026, 0, 0, 0, 0]
kitchen_11 = [2.187400, -2.291220, 0, 0, 0, 0]
bedroom_11 = [-2.435811, -1.795186, 0, 0, 0, 1.557907]
bathroom_11 = [-2.364777, 3.206479, 0, 0, 0, 0]
places_11 = [living_11, kitchen_11, bedroom_11, bathroom_11]
prob_11 = [30 / 55, 10 / 55, 10 / 55, 5 / 55]

## 物体の位置の座標 (penguin_doll)
living_12 = [2.367916, 0.863456, 0, 0, 0, -3.082648]
kitchen_12 = [3.212406, -2.315549, 0, 0, 0, 2.774714]
bedroom_12 = [-2.264622, -2.432036, 0.306387, 0, 0, 1.602510]
bathroom_12 = [-2.794570, 2.573460, 0, 0, 0, 0]
places_12 = [living_12, kitchen_12, bedroom_12, bathroom_12]
prob_12 = [5 / 45, 5 / 45, 30 / 45, 5 / 45]

## 物体の位置の座標 (sheep_doll)
living_13 = [2.338708, 0.101857, 0, 0, 0, -3.113188]
kitchen_13 = [2.734007, -2.490820, 0.074294, 0, 0, 2.777340]
bedroom_13 = [-1.933361, -2.417364, 0.300000, 0, 0, 1.647559]
bathroom_13 = [-2.918357, 2.909400, 0, 0, 0, 0]
places_13 = [living_13, kitchen_13, bedroom_13, bathroom_13]
prob_13 = [5 / 45, 5 / 45, 30 / 45, 5 / 45]

## 物体の位置の座標 (pig_doll)
living_14 = [2.326773, 0.447960, 0, 0, 0, 3.128099]
kitchen_14 = [3.013530, -2.827840, 0, 0, 0, 2.751296]
bedroom_14 = [-2.563965, -2.420747, 0.3, 0, 0, 1.520070]
bathroom_14 = [-2.962426, 3.230660, 0, 0, 0, 0]
places_14 = [living_14, kitchen_14, bedroom_14, bathroom_14]
prob_14 = [5 / 45, 5 / 45, 30 / 45, 5 / 45]

## 物体の位置の座標 (airplane_toy)
living_15 = [1.994466, -0.360955, 0.000096, 0.020061, 0.341599, 1.455727]
kitchen_15 = [1.953379, -2.927162, 0.002139, 0.019313, 0.340810, 0.001836]
bedroom_15 = [-3.212100, -2.087783, 0.001471, 0.019312, 0.340810, 0.001570]
bathroom_15 = [-2.373758, 3.643614, -0.003093, 0.019312, 0.340807, 0.000342]
places_15 = [living_15, kitchen_15, bedroom_15, bathroom_15]
prob_15 = [5 / 45, 5 / 45, 30 / 45, 5 / 45]

## 物体の位置の座標 (car_toy)
living_16 = [1.227374, -0.121645, 0.004814, 0.001980, -0.000559, 0.000839]
kitchen_16 = [2.356606, -2.522389, 0.006733, 0.002266, 0.000015, 0.857630]
bedroom_16 = [-2.963780, -1.584595, 0.005985, 0.002012, -0.000625, 0.001095]
bathroom_16 = [-2.110327, 2.842969, 0.002461, 0.001990, -0.000587, 0.000889]
places_16 = [living_16, kitchen_16, bedroom_16, bathroom_16]
prob_16 = [5 / 45, 5 / 45, 30 / 45, 5 / 45]

## 物体の位置の座標 (truck_toy)
living_17 = [2.384808, -0.311686, 0, 0, 0, 2.406678]
kitchen_17 = [2.203776, -3.296018, 0, 0, 0, 1.596243]
bedroom_17 = [-3.143250, -2.504429, 0, 0, 0, 0]
bathroom_17 = [-3.108750, 3.549850, 0, 0, 0, 0]
places_17 = [living_17, kitchen_17, bedroom_17, bathroom_17]
prob_17 = [5 / 45, 5 / 45, 30 / 45, 5 / 45]

## 物体の位置の座標 (tooth_paste)
living_18 = [1.631962, 0.102705, 0.003737, -0.011131, -0.027742, -1.529262]
kitchen_18 = [2.334591, -2.401680, 0.006195, 0.017211, -0.021353, -1.509233]
bedroom_18 = [-2.104030, -1.757963, 0.005710, -0.037476, -0.027241, -3.023347]
# bathroom_18 = [-2.370607, 2.724758, 0.002151, 0.012253, -0.009277, 1.974071] # 学習用
bathroom_18 = [-2.42, 3.58, 0, 0, -0.03, 1.97] # 探索用
places_18 = [living_18, kitchen_18, bedroom_18, bathroom_18]
prob_18 = [5 / 35, 5 / 35, 5 / 35, 20 / 35]

## 物体の位置の座標 (towel)
living_19 = [1.656315, -0.190269, 0.003411, -0.000802, 0.014082, 0.000052]
kitchen_19 = [2.509693, -3.163208, 0.005836, -0.001590, 0.012108, 0.000016]
bedroom_19 = [-2.908292, -2.082946, 0.006123, -0.000938, -0.000528, 0.000086]
bathroom_19 = [-2.651868, 3.434609, 0.000525, -0.000800, 0.014081, 0.003162]
places_19 = [living_19, kitchen_19, bedroom_19, bathroom_19]
prob_19 = [5 / 35, 5 / 35, 5 / 35, 20 / 35]

## 物体の位置の座標 (cup)
living_20 = [1.639370, 0.274498, 0.003863, -0.006316, -0.017370, -0.000033]
kitchen_20 = [2.014094, -3.109407, 0.726572, -0.009521, -0.019328, 0.000044]
bedroom_20 = [-1.974105, -1.763279, 0.005684, -0.019378, -0.030809, 0.000369]
# bathroom_20 = [-2.063556, 2.989445, 0.001853, -0.015649, -0.015247, -0.931978] # 学習用
bathroom_20 = [-2.47, 3.75, 0, -0, -0.01, -0.93] # 探索用
places_20 = [living_20, kitchen_20, bedroom_20, bathroom_20]
prob_20 = [5 / 35, 5 / 35, 5 / 35, 20 / 35]

## 物体の位置の座標 (treatments)
living_21 = [1.933211, 0.834037, 0.002752, -0.002738, -0.010410, -1.637899]
kitchen_21 = [2.718991, -2.996992, 0.006337, 0.014546, -0.007799, -1.615307]
bedroom_21 = [-2.615960, -2.031615, 0.005718, -0.002440, -0.002066, -3.131718]
bathroom_21 = [-2.627028, 3.101950, 0.000946, -0.002735, -0.008822, 1.643564]
places_21 = [living_21, kitchen_21, bedroom_21, bathroom_21]
prob_21 = [5 / 65, 5 / 65, 5 / 65, 50 / 65]

## 物体の位置の座標 (body_sponge)
living_22 = [1.483343, 0.837575, 0.003528, 0.000654, -0.005946, 1.599634]
kitchen_22 = [2.190729, -2.428094, 0.006117, 0.001545, -0.005697, 2.340102]
bedroom_22 = [-2.424397, -1.630863, 0.005494, -0.000161, -0.006827, -0.107714]
# bathroom_22 = [-2.169262, 3.017801, 0.001792, -0.000010, -0.007213, -0.636462] # 学習用
bathroom_22 = [-2.42, 3.36, 0, 0, -0, -1.23] # 探索用
places_22 = [living_22, kitchen_22, bedroom_22, bathroom_22]
prob_22 = [5 / 65, 5 / 65, 5 / 65, 50 / 65]

## 物体の位置の座標 (bath_slipper)
living_23 = [1.691294, 0.756263, 0.003771, -0.002696, 0.002602, -0.000190]
kitchen_23 = [2.610614, -2.202957, 0.006128, -0.002181, 0.003376, 1.303894]
bedroom_23 = [-2.033465, -1.597597, 0.005672, -0.001973, 0.002767, -0.706314]
# bathroom_23 = [-2.277214, 2.640324, 0.002271, -0.002696, 0.002600, -0.000052] # 学習用
bathroom_23 = [-2.27, 3.86, 0, -0, 0, -0] # 探索用
places_23 = [living_23, kitchen_23, bedroom_23, bathroom_23]
prob_23 = [5 / 65, 5 / 65, 5 / 65, 50 / 65]

#####
living = [living_0, living_1, living_2, living_3, living_4, living_5,
          living_6, living_7, living_8, living_9, living_10, living_11,
          living_12, living_13, living_14, living_15, living_16, living_17,
          living_18, living_19, living_20, living_21, living_22, living_23]
kitchen = [kitchen_0, kitchen_1, kitchen_2, kitchen_3, kitchen_4, kitchen_5,
           kitchen_6, kitchen_7, kitchen_8, kitchen_9, kitchen_10, kitchen_11,
           kitchen_12, kitchen_13, kitchen_14, kitchen_15, kitchen_16, kitchen_17,
           kitchen_18, kitchen_19, kitchen_20, kitchen_21, kitchen_22, kitchen_23]
bedroom = [bedroom_0, bedroom_1, bedroom_2, bedroom_3, bedroom_4, bedroom_5,
           bedroom_6, bedroom_7, bedroom_8, bedroom_9, bedroom_10, bedroom_11,
           bedroom_12, bedroom_13, bedroom_14, bedroom_15, bedroom_16, bedroom_17,
           bedroom_18, bedroom_19, bedroom_20, bedroom_21, bedroom_22, bedroom_23]
bathroom = [bathroom_0, bathroom_1, bathroom_2, bathroom_3, bathroom_4, bathroom_5,
            bathroom_6, bathroom_7, bathroom_8, bathroom_9, bathroom_10, bathroom_11,
            bathroom_12, bathroom_13, bathroom_14, bathroom_15, bathroom_16, bathroom_17,
            bathroom_18, bathroom_19, bathroom_20, bathroom_21, bathroom_22, bathroom_23]
places = [places_0, places_1, places_2, places_3, places_4, places_5,
          places_6, places_7, places_8, places_9, places_10, places_11,
          places_12, places_13, places_14, places_15, places_16, places_17,
          places_18, places_19, places_20, places_21, places_22, places_23]
prob = [prob_0, prob_1, prob_2, prob_3, prob_4, prob_5,
        prob_6, prob_7, prob_8, prob_9, prob_10, prob_11,
        prob_12, prob_13, prob_14, prob_15, prob_16, prob_17,
        prob_18, prob_19, prob_20, prob_21, prob_22, prob_23]

##################################
# scenario3_part1
"""
names: [ "plate", "bowl", "pitcher_base", "banana",
         "apple", "orange", "cracker_box", "pudding_box",
         "chips_bag", "coffee", "muscat", "fruits_juice",
         "penguin_doll", "sheep_doll", "pig_doll", "airplane_toy",
         "car_toy", "truck_toy", "tooth_paste", "towel",
         "cup", "treatments", "sponge", "bath_slipper"]
"""
Location_3_1 = [1, 0, 1, 0,
                0, 0, 0, 0,
                0, 3, 0, 2,
                2, 2, 3, 2,
                2, 3, 0, 3,
                3, 3, 3, 3]
##################################
# objects = [plate, bowl, pitcher_base, banana, apple, orange,
#           cracker_box, pudding_box, chips_bag, coffee, muscat, fruits_juice,
#           penguin_doll, sheep_doll, pig_doll, airplane_toy, car_toy, truck_toy,
#           tooth_paste, towel, cup, treatments, body_sponge, bath_slipper]


## 実験2 (SII2023)
exp2_obj_pose = [[1.59, -3.21, 0.73, 0.0, 0.0, -2.45],
                 [2.70, -3.42, 0.72, 0.0, 0.0, 0.0],
                 [4.68, -2.73, 0.88, 0.0, 0.0, 0.0],
                 [2.53, -3.17, 0.72, 0.0, 0.0, 1.3],
                 [4.45, -3.66, 0.83, 0.0, 0.0, 0.0],
                 [-0.17, -3.63, 0.85, 0.03, 0.05, 0.0],

                 [3.40, 1.61, 0.42, -0.05, -0.74, -1.71],
                 [2.82, 0.75, 0.44, 0.0, 0.0, 0.3],
                 [2.67, 0.35, 0.44, 0.0, 1.38, 0.0],
                 [3.33, 0.93, 0.41, 0.0, 0.0, 0.0],
                 [2.66, -1.07, 0.35, 0.0, 0.0, 0.0],
                 [2.21, 1.90, 0.52, 0.0, 0.0, 0.0],

                 [-1.81, -3.17, 0.32, 0.0, 0.0, 1.64],
                 [-4.7, -3.0, 0.74, 0.0, 0.0, 0.0],
                 [-2.31, -1.58, 0.0, 0.0, 0.0, 0.0],
                 [-3.1, -3.88, 0.0, 0.0, 0.34, 0.0],
                 [-1.43, -1.64, 0.0, 0.0, 0.0, 0.0],
                 [-4.08, -2.42, 0.0, 0.0, 0.0, -1.57],

                 [-2.17, 1.74, 0.84, 0.0, 0.0, 3.13],
                 [-3.27, 2.63, 0.13, -0.89, 0.01, 0.0],
                 [-2.0, 1.78, 0.84, 0.0, 0.0, 0.0],
                 [-1.2, 1.79, 0.84, 0.0, 0.0, -2.9],
                 [-2.54, 2.24, 0.018, 0.027, 1.11, 0.99],
                 [-2.89, 3.66, 0.0, 0.0, 0.0, -3.0]
                 ]






























