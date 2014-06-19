# -*- coding: gbk -*-
"""
temperature part c1
"""
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