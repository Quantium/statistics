#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
from math import gcd
dices = [[1]*4 + [0]*3,[1]*5 + [0]*4,[1]*4 +[0]*4]
s = 0
a = 0
for i in itertools.product(*dices):
    s+=1
    if i[0] + i[1] + i[2] == 2:
        a+=1

f = gcd(a,s)
print(a//f, end="/")
print(s//f)