# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 19:56:34 2013

@author: Administrator
"""

from Tkinter import *
root=Tk()







foodX=[0]
foodY=[0]
foodx=random.randrange(16,571,step)
foody=random.randrange(16,346,step)




def draw_food():
    global foodx,foody,level,k,j,foodname
    canvas.delete('food')
    for _ in range(1,level+1):#食物数量
        random_food()
        for i in range(0,len(snakeX)-1):
            if foodx==snakeX[i] and foody==snakeY[i]:
                random_food()        
        del foodX[k]
        del foodY[k]
        foodX.insert(0,foodx)
        foodY.insert(0,foody)
    for j in range(0,level):
        canvas.create_rectangle(foodX[j],foodY[j],foodX[j]+step,foodY[j]+step,fill='red' ,tags=("food",foodname))     #food view

def random_food():
    global foodx,foody    
    foodx=random.randrange(16,571,step)
    foody=random.randrange(16,346,step)

def iseated():
    global foodx,foody,gamescore,k,level
    for k in range(0,level):
        if foodX[k]==snakeX[0] and foodY[k]==snakeY[0]:
            gamescore+=5
            score()
            break
    return True

k=j=0
foodname='food'+str(j)





