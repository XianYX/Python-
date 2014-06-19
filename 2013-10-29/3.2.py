# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:53:41 2013

@author: Administrator
"""

from Tkinter import *
import random,sys 


"=== View Part ==="        
def draw_wall():
    canvas.create_line((13,13),(13,363),(13,363),(588,363),(588,363),(588,13),(588,13),(13,13),width=5,fill='blue')

def draw_score():
    score()                        # score model
    score_label.config(text='Score:'+str(gamescore)+'    level:'+str(level))    # score view
    
def draw_food():
    global foodx,foody,level
    canvas.delete("food")
    for _ in range(1,level+1):
        random_food()
        for i in range(0,len(snakeX)-1):
            if foodx==snakeX[i] and foody==snakeY[i]:
                random_food()
        canvas.create_rectangle(foodx,foody,foodx+step,foody+step,fill='red' ,tags="food")     #food view

def draw_snake():
    canvas.delete("snake")
    snake()                    # snake model
    for i in range(0,len(snakeX)-1):
        '''ganescore+3'''             # snake view
        canvas.create_rectangle(snakeX[i],snakeY[i],snakeX[i]+step,snakeY[i]+step,fill=('orange'),tags='snake')    

"=== Model Part ==="
# food model
def random_food():
    global foodx,foody    
    foodx=random.randrange(16,571,step)
    foody=random.randrange(16,346,step)

# snake model
def snake():
    global snakeX,snakeY,new_x,new_y
    if iseated()==True:
        snakeX.insert(0,new_x)
        snakeY.insert(0,new_y)
        draw_food()
    else:
        snakeX.insert(0,new_x)
        snakeY.insert(0,new_y)
        del snakeX[-1]
        del snakeY[-1]
        
#score model    
def score():
    global gamescore,level
    if gamescore<10:
        level=1
    elif gamescore<20:
        level=2
    elif gamescore<30:
        level=3
    elif gamescore<40:
        level=4
    else:
        level=5
    score_label.config(text='Score:'+str(gamescore)+'    level:'+str(level))
    
    

"=== Control Part ==="     
def iseated():
    global foodx,foody,gamescore
    if foodx==snakeX[0] and foody==snakeY[0]:
        gamescore+=5
        score()
        return True

def isdead():
    if snakeX[0] < 16 or snakeX[0] > 571 or snakeY[0] < 16 or snakeY[0] > 346:
        return True
    for i in range(1,len(snakeX)-1):
        if snakeX[i] == snakeX[0] and snakeY[i] == snakeY[0]:
            return True       
    return False

def move(event):
    global snakeDirection
    if (event.keycode == 37 or event.keycode == 65) and snakeDirection!='RIGHT':
        snakeDirection='LEFT'
    elif (event.keycode == 39 or event.keycode == 68) and snakeDirection!='LEFT':
        snakeDirection='RIGHT'
    elif (event.keycode == 38 or event.keycode == 87) and snakeDirection!='DOWN':
        snakeDirection='UP'
    elif (event.keycode == 40 or event.keycode == 83) and snakeDirection!='UP':
        snakeDirection='DOWN'

#    draw_snake()
        
def play():
    global new_x,new_y,speed
    while True:
        canvas.focus_set()
        canvas.bind('<Key>',move)
        if snakeDirection=='LEFT':
            new_x = snakeX[0]-step       
        elif snakeDirection=='RIGHT':
            new_x = snakeX[0]+step
        elif snakeDirection=='UP':
            new_y = snakeY[0]-step
        elif snakeDirection=='DOWN':
            new_y = snakeY[0]+step
        if isdead()==True:
            break          
        draw_snake()
        canvas.after(speed)
        canvas.update()               
    gameover()
        

def gameover():
    canvas.delete('food')
    canvas.delete('snake')
    canvas.create_text(300,100,text='Game Over!',font='Verdana 30 bold',tags='text1')
    canvas.create_text(300,200,text='Your score is : '+str(gamescore),font='Verdana 20 bold',tags='text2')
    canvas.create_text(300,275,text='Press R to retry and press Q to exit',font='Verdana 15 bold',tags='text3')
    canvas.bind('<Key>',restart)

def restart(event):
    if event.keycode==81:
        sys.exit()
    if event.keycode==82:
        canvas.delete(ALL)
        global gamescore,step,snakeX,snakeY,new_x,new_y,foodx,foody,snakeDirection,level,speed
        step=15
        gamescore=0
        level=1                
        snakeX=[]
        snakeY=[]
        new_x=16+(5*step)
        new_y=16+(3*step)
        foodx=random.randrange(16,571,step)
        foody=random.randrange(16,346,step)
        for i in range(6,9):
            snakeX.append(16+(i*step))
            snakeY.append(16+(3*step))
        snakeDirection = 'DOWN'
        draw_wall()
        draw_score()
        draw_food()
        draw_snake()
        play()


step=15
gamescore=0
level=1                
snakeX=[]
snakeY=[]
new_x=16+(5*step)
new_y=16+(3*step)
foodx=random.randrange(16,571,step)
foody=random.randrange(16,346,step)
speed=200-(level-1)*10

for i in range(6,9):
    snakeX.append(16+(i*step))
    snakeY.append(16+(3*step))
# to initialize the moving direction
snakeDirection = 'DOWN'  
# to draw the game frame 
window = Tk()
window.geometry("600x400+10+10")
window.maxsize(600,400)
window.minsize(600,400)
window.title("Snake game")

frame1=Frame(window,height=370,width=600)
frame2=Frame(window,height=30,width=600)
canvas=Canvas(frame1,bg='yellow',width=600,height=370)
score_label=Label(frame2,text='Score:'+str(gamescore)+'    level:'+str(level))

frame1.pack()
frame2.pack(fill=BOTH)
score_label.pack(side=LEFT)
canvas.pack(fill=BOTH)
 
draw_wall()
draw_score()
draw_food()
draw_snake()

play()

window.mainloop()
