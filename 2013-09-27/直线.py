# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is to draw a line with the given coordinates and calculate the length between them.
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.1
date:2013-9-27 03:09:54
"""

x1,y1=eval(raw_input("please enter the coordinates of the first point:"))  #input the coordinates of the first point
x2,y2=eval(raw_input("please enter the coordinates of the second point:"))  #input the coordinates of the second point
length=((x1-x2)**2+(y1-y2)**2)**0.5  #calculate the length between the two point

import turtle  #import turtle module
turtle.pensize(2)  #set pen size to 2 pixels
turtle.penup()  #pull the pen up
turtle.goto(x1,y1)  #put the pen to (x1,y1)
turtle.pendown()  #pull the pen down
turtle.goto(x2,y2)  #draw the line

turtle.penup()  #pull the pen up
turtle.goto(x1,y1-10)  #put the pen to the top of the first point 
turtle.pendown()  #pull the pen down
turtle.write((x1,y1),False)  #write the coordinate of the first point

turtle.penup()  #pull the pen up
turtle.goto(x2,y2+10)  #put the pen to the top of the second point 
turtle.pendown()  #pull the pen down
turtle.write((x2,y2),False)  #write the coordinate of the second point

turtle.penup()  #pull the pen up
turtle.goto(0.5*(x1+x2)+10,0.5*(y1+y2)+10)  #put the pen at the middle of the line
turtle.pendown()  #pull the pen down
turtle.write("the length of the line is : "+str(length),False,align="left")  #write the length of the line

