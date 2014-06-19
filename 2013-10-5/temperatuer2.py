# -*- coding: gbk -*-
"""
Spyder Editor
python 2.7
This program is for coverting the temperature . 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-3 23:23:15
"""
#input the model and the value
m=raw_input("please input the modle:")
#select the modle 
if m=="1":
    #modle 1 is to switch the degree Fahrenheit to degree centigrade 
    #modle 1 begins
    #input the value of the temperature and switch the type of valu to float
    try:
        f=float(raw_input("please input the value:"))
        #if the value is unable to use output "error"
    except:
        print("error")
        #if the value is number,continue to covert the temperature to degree Keivin
    else:
        c=(f-32)*5/9+273.15
        #jurdge if the value is reasonable
        if c>0:
            #if the value is reasonable, output the result
            t=c-273.15
            print("The temperature is :"+str(format(t,".2f"))+"℃")
        else:
            #if the value is unreasonable,output "error"
            print("error")
    #mode 1 finishes
elif m=="2":
    #modle 2 is to switch the degree centigrade to degree Fahrenheit
    #modle 2 begins
    #input the value of the temperature and switch the type of valu to float
    try:
        t=float(raw_input("please input the value:"))
        #if the value is unable to use output "error"
    except:
        print("error")
        #if the value is number,continue to covert the temperature to degree Keivin
    else:
        c=t+273.15
        #jurdge if the value is reasonable
        if c>0:
            #if the value is reasonable, output the result
            f=(9*(c-273.15)/5+32)
            print("The temperature is :"+str(format(f,".2f"))+"℉")
        else:
            #if the value is unreasonable,output "error"
            print("error")
    #mode 2 finishes
else :
    #if the modle is unable to use, output "error"
    print("error")        
#finish