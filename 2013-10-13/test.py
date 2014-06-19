# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:12:27 2013

@author: Administrator
"""
#modle two
#import the fucation of sqrt
from math import sqrt
sum=0
#set the loop range
for i in range(3,100):
    if i%2==0:
#reject the obb number
        continue
    else:
#select the prime to add up
        j=int(sqrt(i))+1
        m=0        
        for n in range(2,j):
            if i%n==0:
                m+=1
                break
        if m==0:
            sum+=i
#add 2 to sum
print(2+sum)