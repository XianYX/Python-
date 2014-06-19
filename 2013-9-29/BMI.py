# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for calcuate the BMI. 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-9-29 14:11:35
"""

#enter the weight 
w=eval(raw_input("Enter weighe in pounds :" ))
#enter the height 
h=eval(raw_input("Enter heighe in inch :" ))
#convert the unit of the weight ang height
if w<0 or h<0:
    print("Error")
else:
    w0=w*0.45359237
    h0=h*0.0254
    #calcuate the BMI
    BMI=format(w0/(h0**2),".4f")
    #output the result
    print("BMI  is :"+str(BMI))
