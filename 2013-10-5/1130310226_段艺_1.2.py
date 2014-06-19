# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for coverting the temperature . 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.1
date:2013-10-4 18:13:46
"""
#input the model and the value
m=raw_input()
#select the modle 
if m=="1":
    #modle 1 is to switch the degree Fahrenheit to degree centigrade 
    #modle 1 begins
    #input the value of the temperature and switch the type of value to float
    try:
        f=float(raw_input())
        #if the value is unable to use output "Error"
    except:
        print("Error")
        #if the value is number,continue to covert the temperature to degree Keivin
    else:
        c=(f-32)*5/9+273.15
        #jurdge if the value is reasonable
        if c>0:
            #if the value is reasonable, output the result
            t=c-273.15
            print(str(format(t,".2f")))
        else:
            #if the value is unreasonable,output "Error"
            print("Error")
    #mode 1 finishes
elif m=="2":
    #modle 2 is to switch the degree centigrade to degree Fahrenheit
    #modle 2 begins
    #input the value of the temperature and switch the type of valu to float
    try:
        t=float(raw_input())
        #if the value is unable to use output "Error"
    except:
        print("Error")
        #if the value is number,continue to covert the temperature to degree Keivin
    else:
        c=t+273.15
        #jurdge if the value is reasonable
        if c>0:
            #if the value is reasonable, output the result
            f=(9*(c-273.15)/5+32)
            print(str(format(f,".2f")))
        else:
            #if the value is unreasonable,output "Error"
            print("Error")
    #mode 2 finishes
else :
    #if the modle is unable to use, output "Error"
    print("Error")        
#finish