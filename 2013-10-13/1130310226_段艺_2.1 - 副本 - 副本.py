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
from time import clock
clock()
#modle one
i=0
n=1
#define the range of number to add up
while n<1000:
#add up the number use the loop struction 
    if n%3==0 or n%5==0:
        i += n
    n+=1
print(i)
#modle two
#def prime
def prime(i):
    j=int(i**0.5)
    m=0
    n=3
    while n<j:
        if i%n==0:
            m+=1
            break
        n+=2
    return m==0
sum=0
#set the loop range
for i in range(3,2000000,2):
        p=prime(i)
        if p==True:
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
t=clock()