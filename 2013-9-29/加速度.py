# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for calcuate the average acceleration . 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-9-29 13:23:22
"""
#enter the starting velocity , the ending velocity and the time span . 
v0,v1,t=eval(raw_input("Please enter the starting velocity v0 ,the ending velocity v1 and the time span t (separed by comma):"))
#calcuate the average acceleration
a=format((v1-v0)/t,".4f")
#print the result
print("The average acceleration is :"+str(a))
