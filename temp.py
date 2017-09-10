# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:58:04 2017

@author: Administrator
"""

import random

def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1,maxCost)))
    return items

for numItems in range(5,46,5):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal