# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for calculatoring some questions.
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-12 12:19:06
"""
from math import pi
#question one
print("Question one")
def v(r):
    volume=4*pi*r**3/3
    return volume
#output the result
print("the volume of a sphere with radius is :"+format(v(5),".2f"))
#question two
print("Question two")
def total_cost(n):
    sum=24.95*0.6*n+33+0.75*(n-1)
    return sum
#print the result    
print("the total cost for 60 copies is:"+format(total_cost(60),".2f"))
#question three
print("Question three")
sth=6
stm=52
sts=sth*3600+stm*60
t1=8*60+15
t2=7*60+12
eds=sts+2*t1+3*t2
edh=eds//3600
edm=(eds%3600)//60
eds=(eds%3600)%60
print("time for breakfastis:"+str(edh)+":"+str(edm)+":"+str(eds))