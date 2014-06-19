# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for three modle.
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-13 19:25:46
"""
#modle one
i=0
#define the range of number to add up
for n in range(1,1000):
#add up the number use the loop struction 
    if n%3==0 or n%5==0:
        i += n
print(i)
#modle two
sum=0
#set the loop range
for i in range(3,2000000):
    if i%2==0:
#reject the obb number
        continue
    else:
#select the prime to add up
        j=int(i**0.5)+1
        m=0        
        for n in range(2,j):
            if i%n==0:
                m+=1
                break
        if m==0:
            sum+=i
#add 2 to sum
print(2+sum)
#modle three
#import datetime modle to solve the problem^_^
from datetime import date
sum=0
#set the range of year and month
for year in range(1901,2001):
    for month in range(1,13):
#set the date
        d=date(year,month,1)
#compute the name of a day 
        c=d.isoweekday()
        if c==7:
            sum += 1
print(sum)