# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for drawing four doing n. 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-9 21:25:59
"""
#make sure the number input is right
try:
    #input the value of number and loop times
    x=float(raw_input("please input the value:"))
    n=eval(raw_input("please input the time of loop:"))
except:
    #if input the wrong thing output "Error"
    print("Error")   
else:
    #start to comput
    i=0
    while i<n:
        x=x**2+2
        i += 1
    #output the value
    print("the value is:"+format(x,".2f"))
#finish the program
print("End")
    
    
