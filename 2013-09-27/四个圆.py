# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for drawing four circles . 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-9-27 01:30:39
"""

import turtle  #import turtle module
turtle.pensize(2)  #set pen size to 2 pixels
turtle.penup()  #pull the pen up
turtle.goto(-100,0)  #put the pen to (-100,0)
turtle.pendown()  #pull the pen down
turtle.circle(100)  #draw the first circle with the radius of 100 pixels

turtle.penup()  #pull the pen up
turtle.goto(100,0)  #put the pen to (100,0)
turtle.pendown()  #pull the pen down
turtle.circle(100)  #draw the second circle with the radius of 100 pixels

turtle.penup()  #pull the pen up
turtle.goto(-100,-200)  #put the pen to (-100,-200)
turtle.pendown()  #pull the pen down
turtle.circle(100)  #draw the third circle with the radius of 100 pixels

turtle.penup()  #pull the pen up
turtle.goto(100,-200)  #put the pen to (-100,-200)
turtle.pendown()  #pull the pen down
turtle.circle(100)  #draw the fourth circle with the radius of 100 pixels

