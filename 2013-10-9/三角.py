# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for computing the angle of the triangle
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013年10月11日 21:22:04
"""
#import the necessary function
from math import sqrt
from math import acos
from math import degrees
#input the coordinate of the points
try:
    x1,y1=eval(raw_input("please enter the coordinate for the first point:"))
    x2,y2=eval(raw_input("please enter the coordinate for the second point:"))
    x3,y3=eval(raw_input("please enter the coordinate for the third point:"))
except:
    print("Error")
else:
    #jurdge if the point is the same point
    if (x1==x2 and y1==y2)or(x1==x3 and y1==y3)or(x2==x3 and y2==y3):
        print("The same print!")
    else:
        try:
            #compute the length of three sides
            a=sqrt((x1-x2)**2+(y1-y2)**2)
            b=sqrt((x1-x3)**2+(y1-y3)**2)
            c=sqrt((x3-x2)**2+(y3-y2)**2)
            #compute the radians of the triangle
            A=acos((a*a-b*b-c*c)/(-2*b*c))
            B=acos((b*b-a*a-c*c)/(-2*a*c))
            C=acos((c*c-a*a-b*b)/(-2*a*b))
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