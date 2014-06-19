# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for calcuating the future investment value. 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-9-29 14:51:56
"""

#enter the investment amount 
a=eval(raw_input("Enter investment amount :" ))
#enter the annual interest rate
r=eval(raw_input("Enter annual interest rate :" ))
#enter the number of years
y=eval(raw_input("Enter number of years :" ))
#convert the unit of time and interest rate
m=12*y
r *= 0.01
r /= 12
#compute the future investment value
value=str(format(a*(1+r)**m,".2f"))
#output the result
print("Accumulated value is :"+value)
