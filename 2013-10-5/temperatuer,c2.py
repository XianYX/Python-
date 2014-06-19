# -*- coding: gbk -*-
"""
temperature part c2
"""
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