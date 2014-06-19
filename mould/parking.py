# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:59:47 2013

@author: Administrator
"""
import random
def parking(beg,end):
    if end-beg<1:
        return 0
    else:
        x=random.uniform(beg,end-1)
        return parking(beg,x)+parking(x+1,end)+1  
s=0

for _ in range(0,100000):
    s+=parking(0,100)
print s/100000.0