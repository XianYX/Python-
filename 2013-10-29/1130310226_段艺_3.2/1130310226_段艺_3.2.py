# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is a snake game
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-11-1 01:26:38
"""

#import the modles which will be made
from Tkinter import *
import random,sys 

"=== View Part ==="
        
def draw_wall():
    '''
    This function is to draw the wall.
    '''
    canvas.create_line((13,13),(13,363),(13,363),(588,363),(588,363),(588,13),(588,13),(13,13),width=5,fill='blue')

def draw_score():
    '''
    This function is to display the score and level
    '''
    score()                        
    score_label.config(text='Score: %d    Level:%d'%(gamescore,level))    
    
def draw_food():
    '''
    This function is to draw the food.
    '''
    global foodx,foody,level,k,j
    #delete the food which is already eated
    canvas.delete('food')
    random_food()
    #delete the old food's coordinate
    del foodX[k]
    del foodY[k]
    #put the new coordinate in the list
    foodX.insert(k,foodx)
    foodY.insert(k,foody)
    #draw the food ,number of food is decided by level
    for j in range(0,level):
        #when the level is up , put a new coordinate in the list
        try:
            canvas.create_rectangle(foodX[j],foodY[j],foodX[j]+step,foodY[j]+step,fill='red' ,tags=("food"))     
        except:
            #set a new food coordinate
            random_food()
            #add the new coodinate of the food in the list
            foodX.insert(j,foodx)
            foodY.insert(j,foody)
            #draw the food
            canvas.create_rectangle(foodX[j],foodY[j],foodX[j]+step,foodY[j]+step,fill='red' ,tags=("food"))            
        else:
            canvas.create_rectangle(foodX[j],foodY[j],foodX[j]+step,foodY[j]+step,fill='red' ,tags=("food"))

def draw_snake():
    '''
    This function is to draw a snake.
    '''
    canvas.delete("snake")
    snake()
    #draw the snake by the coodinate in the list
    for i in range(0,gamescore/10+3):           
        canvas.create_rectangle(snakeX[i],snakeY[i],snakeX[i]+step,snakeY[i]+step,fill=('orange'),tags='snake')    

"=== Model Part ==="

def random_food():
    '''
    This function is to get a random coodinate of the food
    '''
    global foodx,foody,snakeX,snakeY
    foodx=random.randrange(16,571,step)
    foody=random.randrange(16,346,step)
    #jurdge if the new food corves on the snake,if so change the food
    for i in range(0,len(snakeX)-1):
        if foodx==snakeX[i] and foody==snakeY[i]:
            random_food()

def snake():
    '''
    This function is to set the snake
    '''
    global snakeX,snakeY,new_x,new_y
    #if eat a food,app a new coodinate in the list
    if iseated()==True:
        snakeX.insert(0,new_x)
        snakeY.insert(0,new_y)
        draw_food()
    else:
        snakeX.insert(0,new_x)
        snakeY.insert(0,new_y)
        #delete the old coodinate of the list
        del snakeX[-1]
        del snakeY[-1]
            
def score():
    '''
    This function is to compute the score,level and speed
    '''
    global gamescore,level,speed
    level=1+gamescore/100
    if level<17:
        speed=200-(level-1)*10
    else:
        speed=50
    
"=== Control Part ==="

def iseated():
    '''
    This function is to jurdje if the snake is eated a food.
    '''
    global foodx,foody,gamescore,k,level
    #jurdge is the food is be eaten
    for k in range(0,level):
        if foodX[k]==snakeX[0] and foodY[k]==snakeY[0]:
            #when eat a food the score plus one
            gamescore+=10
            draw_score()
            return True
            break

def isdead():
    '''
    This function is to jurdje if the snake is dead
    '''
    if snakeX[0] < 16 or snakeX[0] > 571 or snakeY[0] < 16 or snakeY[0] > 346:
        return True
    for i in range(1,len(snakeX)-1):
        if snakeX[i] == snakeX[0] and snakeY[i] == snakeY[0]:
            return True       
    return False

def move(event):
    '''
    This function is to change the direction the snake move
    '''
    global snakeDirection
    if (event.keycode == 37 or event.keycode == 65) and snakeDirection!='RIGHT':
        snakeDirection='LEFT'
    elif (event.keycode == 39 or event.keycode == 68) and snakeDirection!='LEFT':
        snakeDirection='RIGHT'
    elif (event.keycode == 38 or event.keycode == 87) and snakeDirection!='DOWN':
        snakeDirection='UP'
    elif (event.keycode == 40 or event.keycode == 83) and snakeDirection!='UP':
        snakeDirection='DOWN'
        
def play():
    '''
    This function is the main part of the game
    '''
    global new_x,new_y,speed,k,j
    #main loop only stop when dead
    while True:
        #set the focus in the canvas
        canvas.focus_set()
        #get the key and and change the direction
        canvas.bind('<Key>',move)
        #move 
        if snakeDirection=='LEFT':
            new_x = snakeX[0]-step       
        elif snakeDirection=='RIGHT':
            new_x = snakeX[0]+step
        elif snakeDirection=='UP':
            new_y = snakeY[0]-step
        else:
            new_y = snakeY[0]+step
        if isdead()==True:
        #if the snake is dead break the game .
            break          
        draw_snake()
        #set the speed
        canvas.after(speed)
        canvas.update()
    #if the snake is dead, use the 'gameover' function
    gameover()
        
def gameover():
    '''
    This function is to display the information of when dead
    '''
    #delete the items on the canvas and show the score.
    canvas.delete('food')
    canvas.delete('snake')
    canvas.create_text(300,100,text='Game Over!',font='Verdana 30 bold')
    canvas.create_text(300,200,text='Your score is : '+str(gamescore),font='Verdana 20 bold')
    canvas.create_text(300,275,text='Press R to retry and press Q to exit',font='Verdana 15 bold')
    canvas.create_text(400,325,text='Design by DuanYi \nEmail:Duanyi@hit.edu.cn',font='Verdana 10 bold')
    canvas.bind('<Key>',restart)

def restart(event):
    '''
    This function is to restart the game.
    ''' 
    global k,j
    if event.keycode==81:
        #if user press Q ,exit
        sys.exit()
    if event.keycode==82:
        #delete all the items.
        canvas.delete(ALL)
        global gamescore,step,snakeX,snakeY,new_x,new_y,foodx,foody,snakeDirection,level,speed,foodX,foodY
        #reset all the variable
        step=15
        gamescore=0
        level=1
        k=j=0
        speed=200                
        snakeX=[]
        snakeY=[]
        new_x=16+(5*step)
        new_y=16+(3*step)
        foodX=[0]
        foodY=[0]   
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
        #replay 
        play()
#main part of the game
#set the variable
step=15
gamescore=0
level=1
k=j=0
speed=200
snakeX=[]
snakeY=[]
new_x=16+(5*step)
new_y=16+(3*step)
foodX=[0]
foodY=[0]
foodx=random.randrange(16,571,step)
foody=random.randrange(16,346,step)
# to initialize the snake
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
score_label=Label(frame2,text='Score: %d    Level:%d'%(gamescore,level))

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