# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:33:25 2013

@author: Administrator
"""
from datetime import date,datetime.isoweekday
sum=0
for year in range(1901,2001):
    for month in range(1,13):
        d=date(year,month,1)
        c=d.isoweekday()
        if c==7:
            sum += 1
print(sum)
