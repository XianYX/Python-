# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 19:12:57 2013

@author: Administrator
"""
from Tkinter import *
import random

def draw_wall():
    canvas.create_line((10,10),(10,365),(10,365),(590,365),(590,365),(590,10),(590,10),(10,10),width=5,fill='blue')
    
def draw_score():
#    score()                        # score model
    score_label.config(text='Score:'+str(gamescore))    # score view
    
def draw_food():
    canvas.delete("food")
    foodx,foody=random_food()    #food model
    canvas.create_rectangle(foodx,foody,foodx+15,foody+15,fill='red',tags="food")     #food view
def random_food():      
    foodx=random.randrange(15,575,15)
    foody=random.randrange(15,350,15)
    return foodx,foody

def move(event):
    if (event.keycode == 37 or event.keycode == 65) and moveRight==False:
        moveLeft = True
        moveRight = False
        moveUp = False
        moveDown = False
    if (event.keycode == 39 or event.keycode == 68) and moveLeft==False:
        moveLeft = False
        moveRight = True
        moveUp = False
        moveDown = False
    if (event.keycode == 38 or event.keycode == 87) and moveDown==False:
        moveLeft = False
        moveRight = False
        moveUp = True
        moveDown = False
    if (event.keycode == 40 or event.keycode == 83) and moveUp==False:
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = True

    new_x = snackX[0]
    new_y = snackY[0]

    if moveLeft == True:
        new_x = snackX[0]-15
    if moveRight == True:
        new_x = snackX[0]+15
    if moveUp == True:
        new_y = snackY[0]-15
    if moveDown == True:
        new_y = snackY[0]+15
        return new_x,new_y

    
stap=15
gamescore=0


window = Tk()
window.geometry("600x400+10+10")
#window.maxsize(600,400)
#window.minsize(600,400)
window.title("Snake game")

frame1=Frame(window,height=370,width=600)
frame2=Frame(window,height=30,width=600)
canvas=Canvas(frame1,bg='yellow',width=600,height=370)
score_label=Label(frame2,text='Score:'+str(gamescore))


frame1.pack()
frame2.pack(fill=BOTH)
score_label.pack(side=LEFT)
canvas.pack(fill=BOTH)

draw_wall()
draw_score()
draw_food()

window.mainloop()