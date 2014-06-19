# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for calcuate the BMI. 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-12 17:19:03
"""
try:
    #enter the weight 
    w=float(raw_input("Enter weighe in kilograms :" ))
    #enter the height 
    h=float(raw_input("Enter heighe in inch maters :" ))
except:
    print("Error")
else:
    if w<0 or h<0:
        print("Error")
    else: 
        #calcuate the BMI
        BMI=w/(h**2)
        #give the suggestion
        if BMI<18.5:
            sug="Underweight"
        elif BMI<24.9:
            sug="Normal"
        elif BMI<29.9:
            sug="Overweight"
        else:
            sug="Obese"    
        #output the result
        print("BMI  is :"+format(BMI,".2f"))
        print("You are "+sug+".")
