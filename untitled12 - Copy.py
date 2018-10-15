# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:48:42 2018

@author: ml17b3g
"""

import operator
import random
#Set up variables.
y0=50
x0=50
#Random walk one step.
if random.random()<0.5:
    y0 +=1
else:
    y0-=1
print(y0)

agents = []
agents.append([random.randint(0,99),random.randint(0,99)])
print(max(agents,key=operator.itemgetter(1)))