# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for calcuate the minimum runway length for the airplane . 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-9-29 14:11:13
"""

#enter the average acceleratio and the take-off speed . 
v,a=eval(raw_input("Please enter the take-off speed v and the average acceleration a (separed by comma):"))
#calcuate the minimum runway length for the airplane
l=format(v**2/(2*a),".3f")
#print the result
print("The minimum runway length for the airplane is :"+str(l))

