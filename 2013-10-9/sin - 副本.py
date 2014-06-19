# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for drawing graph of sin again and again.
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-13 03:32:02
"""
#import the necessary functions
from math import sin,pi
from turtle import *
#set the canvas
setworldcoordinates(-4*pi,-2*pi,4*pi,2*pi)
#set the pensize
pensize(2)
#draw X
pu()
goto(-4*pi,0)
pd()
goto(4*pi,0)
pu()
goto(4*pi-0.3,0.1)
pd()
goto(4*pi,0)
pu()
goto(4*pi-0.3,-0.1)
pd()
goto(4*pi,0)
#draw Y
pu()
goto(0,-2*pi)
pd()
goto(0,2*pi)
pu()
goto(-0.1,2*pi-0.3)
pd()
goto(0,2*pi)
pu()
goto(0.1,2*pi-0.3)
pd()
goto(0,2*pi)

pu()
goto(-2*pi,-0.4)
pd()
write("-2pi")
pu()
goto(2*pi,-0.4)
pd()
write("2pi")

while True:
    x=-3.5*pi
    pu()
    goto(x,sin(x))
    pd()
    while x<3.5*pi:
        x += 0.03
        goto(x,sin(x))
