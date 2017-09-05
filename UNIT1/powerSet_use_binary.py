# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:00:58 2017

@author: Administrator
"""

def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
            yield combo
            
foo = powerSet([1, 2, 3])
