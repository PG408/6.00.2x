# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 13:22:30 2017

@author: Administrator
"""
from itertools import chain, combinations
def powerset_generator(i):
    for subset in chain.from_iterable(
            combinations(i, r) for r in range(len(i) + 1)):
        yield list(subset)

def printPowerSet(i):
    for i in powerset_generator(i):
        print(i)