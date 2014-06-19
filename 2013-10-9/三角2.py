# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for computing the angle of the triangle
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.1
date:2013年10月11日 21:22:04
"""
#import the necessary function
from math import sqrt
from math import acos
from math import degrees
"""
this function is to compute the length of the sides.
"""
def length(a,b,c,d):
    l=sqrt((a-b)**2+(c-d)**2)
    return l
"""
this function is to compute the radians of the angles.
"""
def rad(a,b,c):
    r=acos((a*a-b*b-c*c)/(-2*b*c))
    return r
"""
this function is to compute the slope of the sides.
"""    
def slope(a,b,c,d):
    k=(c-d)/(a-b)
    return k
"""
this function is to out put the result.
"""
def compute(x1,x2,x3,y1,y2,y3):      
    try:
        #compute the length of three sides
        a=length(x1,x2,y1,y2)
        b=length(x1,x3,y1,y3)
        c=length(x2,x3,y2,y3)
        #compute the radians of the triangle
        A=rad(a,b,c)
        B=rad(b,c,a)
        C=rad(c,a,b)
    except:
        print("Error")
    else:
        #output the result in radians
        print("the radians of A,B,C is:"+format(A,".2f")+"  "+format(B,".2f")+"  "+format(C,".2f"))
        #switch radians into degrees
        A1=degrees(A)
        B1=degrees(B)
        C1=degrees(C)
        #output the result in degrees
        print("the degrees of A,B,C is:"+format(A1,".2f")+"  "+format(B1,".2f")+"  "+format(C1,".2f"))    

#input the coordinate of the points
try:
    x1,y1=eval(raw_input("please enter the coordinate for the first point:"))
    x2,y2=eval(raw_input("please enter the coordinate for the second point:"))
    x3,y3=eval(raw_input("please enter the coordinate for the third point:"))
except:
    print("Please enter the number!")
else:
    #jurdge if the points are the same point.
    if (x1==x2 and y1==y2)or(x1==x3 and y1==y3)or(x2==x3 and y2==y3):
        print("Don't input the same print!")
    #jurdge if the points are on the same line.
    elif (x1==x2==x3)or(y1==y2==y3):
        print("Three points are on the same line!")       
    else:
        try:
            k1=slope(x1,x2,y1,y2)
        except:
            try:
                k2=slope(x2,x3,y2,y3)
            except:
                print("Three points are on the same line!")
            else:
                compute(x1,x2,x3,y1,y2,y3)
        else:
            try:
                k2=slope(x2,x3,y2,y3)
            except:
                compute(x1,x2,x3,y1,y2,y3)
            else:
                if k1==k2:
                    print("Three points are on the same line!")
                else:
                    compute(x1,x2,x3,y1,y2,y3)
        
        
        
        
        
        
