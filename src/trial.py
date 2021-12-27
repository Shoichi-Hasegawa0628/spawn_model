#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from __init__ import *

print("start")
# 9, 10, 11
o = 9
# 配置する場所を決める
print(prob[o])
max_prob = max(prob[o])
print(max_prob)
print(prob[o].count(max_prob))
if prob[o].count(max_prob) > 1:
    print("aaaaaaaaaaaaaaaaaaa")
    indexes = [i for i, e in enumerate(prob[o]) if e == max_prob]
    print(indexes)
    s = random.choice(indexes)
    print(s)

else:
    s = prob[o].index(max_prob)
