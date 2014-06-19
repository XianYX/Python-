# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 00:01:49 2013

@author: Administrator
"""
from SimpleDialog import *
from tkSimpleDialog import *
from Tkinter import *
import random,sys

"=== View Part ==="
def draw_wall():
    canvas.create_line((13,13),(13,363),(13,363),(588,363),(588,363),(588,13),(588,13),(13,13),width=5,fill='blue')

def first_page():
    draw_wall()
    canvas.create_text(200,100,text='Snake',font='Times 50 bold')
    canvas.create_text(200,200,text='Game',font='Times 50 bold ')
    canvas.create_text(450,100,text='1.New ',font='Courier 25 bold')
    canvas.create_text(450,150,text='2.Load',font='Courier 25 bold')
    canvas.create_text(450,200,text='3.Rank',font='Courier 25 bold')
    canvas.create_text(450,250,text='4.Exit',font='Courier 25 bold')
    canvas.focus_set()
    canvas.bind('<Key>',start)
    
def rank():
    canvas.delete(ALL)
    draw_wall()

    canvas.focus_set()
    canvas.bind('<Key>',rank_key_event)
    try:
        f = open('rank.txt','r')
    except:
        f = open('rank.txt','a')
        f.close()
        canvas.create_text(300,150,text='empty',font='Courier 25 bold')
        canvas.create_text(480,350,text='Press b to back',font='Courier 15 bold')
    else:
        user_lst = [line.strip() for line in f.readlines()]
        f.close()
        if len(user_lst) == 0:
            canvas.create_text(300,150,text='empty',font='Courier 25 bold')
            canvas.create_text(480,350,text='Press b to back',font='Courier 15 bold')
        else:
            user_lst.sort(key = lambda x:int(x.split()[1]),reverse=True)
            canvas.create_text(450,340,text='Press b to back \n  and d to del',font='Courier 15 bold')
            canvas.create_text(300,40,text='Name\tScore\tLevel\tDifficulty',font='Courier 15 bold')            
            lst_y = 80
            for i in user_lst:
                canvas.create_text(300,lst_y,text=i,font='Courier 15 bold')
                lst_y += 30

def show_words():
    canvas.delete(ALL)
    draw_wall()
    word_lst_random = []
    global difficult,speed0,speed
    if difficult == 'easy':
        speed0 = 200
        speed = 200
        f = open('easy1671.txt','r')
        word_lst = [line.strip() for line in f.readlines()]
        f.close()
        for i in range(0,3):
            random_word = word_lst[random.randrange(0,1672)]
            word_lst_random.append(random_word)
    elif difficult =='middle':
        speed0 = 150
        speed = 150
        f = open('middle2104.txt','r')
        word_lst = [line.strip() for line in f.readlines()]
        f.close()
        for i in range(0,4):
            random_word = word_lst[random.randrange(0,2105)]
            word_lst_random.append(random_word)
    elif difficult == 'hard':
        speed0 = 100
        speed = 100
        f = open('hard431.txt','r')
        word_lst = [line.strip() for line in f.readlines()]
        f.close()
        for i in range(0,5):
            random_word = word_lst[random.randrange(0,432)]
            word_lst_random.append(random_word)
    lst_y = 80
    for i in word_lst_random:
        canvas.create_text(300,lst_y,text=i,font='Courier 25 bold')
        lst_y += 50
    canvas.create_text(450,350,text='Ready? Press \'T\' to test!',font='Courier 12 bold')
    canvas.focus_set()
    canvas.bind('<Key>',test)

def draw_score():
    score()                        
    score_label.config(text='Score: %d    Level:%d'%(gamescore,level))

def draw_snake():
    '''
    This function is to draw a snake.
    '''
    canvas.delete("snake")
    snake()
    canvas.create_rectangle(snakeX[0],snakeY[0],snakeX[0]+step,snakeY[0]+step,fill=('green'),tags='snake')
    for i in range(1,gamescore+3):           
        canvas.create_rectangle(snakeX[i],snakeY[i],snakeX[i]+step,snakeY[i]+step,fill=('orange'),tags='snake')

def draw_food():
    '''
    This function is to draw the food.
    '''
    global foodx,foody,level,k,j
    #delete the food which is already eated
    canvas.delete('food')
    update_food()
    #draw the food ,number of food is decided by level
    for j in range(0,3):
        canvas.create_rectangle(foodX[j],foodY[j],foodX[j]+step,foodY[j]+step,fill='red' ,tags=("food"))            

"=== Model Part ==="
def score():
    '''
    This function is to compute the score,level and speed
    '''
    global gamescore,level,speed,speed0,speed
    level=1+gamescore/10
    if speed > 60:
        speed = speed0 - (level-1)*10
    else:
        speed=50

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

def random_food():
    '''
    This function is to get a random coodinate of the food
    '''
    global foodx,foody,snakeX,snakeY,foodX,foodY
    foodx=random.randrange(16,571,step)
    foody=random.randrange(16,346,step)
    #jurdge if the new food corves on the snake,if so change the food
    for i in range(0,len(snakeX)-1):
        if foodx==snakeX[i] and foody==snakeY[i]:
            random_food()
    for i in range(0,len(foodX)-1):
        if foodx == foodX[i] and foody == foodY[i]:
            random_food()


"=== Control Part ==="
def start(event):
    if event.keycode == 49:
        new()
    elif event.keycode == 50:
        load()
    elif event.keycode == 51:
        rank()
    elif event.keycode == 52:
        sys.exit()

def rank_key_event(event):
    if event.keycode == 66:
        canvas.delete(ALL)
        first_page()
    elif event.keycode == 68:
        f = open('rank.txt','r')
        user_lst = [line.strip() for line in f.readlines()]
        f.close()
        if len(user_lst) == 0:
            canvas.delete(ALL)
            draw_wall()
            canvas.create_text(300,150,text='empty',font='Courier 25 bold')
            canvas.create_text(480,350,text='Press b to back',font='Courier 15 bold')
            canvas.focus_set()
            canvas.bind('<Key>',rank_key_event)            
        else:
            rank_del()
        
def rank_del():
    f = open('rank.txt','r')
    user_lst = [line.strip() for line in f.readlines()]
    f.close()
    user_lst.sort(key = lambda x:int(x.split()[1]),reverse=True)
    name_lst = []
    for item in user_lst:
        name_lst.append(item.split()[0])  
    dlg = SimpleDialog(canvas,text='which one to del',buttons=name_lst,default=0,)
    del_index = dlg.go()
    del user_lst[del_index]
    user_lst.sort(key = lambda x:int(x.split()[1]),reverse=True)
    for i in range(0,len(user_lst)-1):
        user_lst[i] += '\n'
    f = open('rank.txt','w')
    f.writelines(user_lst)
    f.close()
    canvas.delete(ALL)
    rank()
        
def new():
    global new_name,new_item
    canvas.delete(ALL)
    draw_wall()
    new_name = askstring(title = 'new',prompt = 'input your name')
    if new_name == '' or new_name == None:
        first_page()
    else:
        canvas.create_text(300,100,text='please choose the difficulty',font='Courier 20 bold')
        canvas.create_text(300,200,text='\'E\'for easy\n\'M\'for middle\n\'H\'for hard',font='Courier 20 bold')
        canvas.create_text(480,350,text='Press b to back',font='Courier 15 bold')
        canvas.focus_set()
        canvas.bind('<Key>',new_event)

def new_event(event):
    global difficult
    if event.keycode == 66:
        canvas.delete(ALL)
        first_page()
    elif event.keycode == 69:
        difficult = 'easy'
        show_words()
    elif event.keycode == 77:
        difficult = 'middle'
        show_words()
    elif event.keycode == 72:
        difficult = 'hard'
        show_words()

def load():
    global new_name,difficult,level,user_score,user_level,user_index
    canvas.delete(ALL)
    draw_wall()
    try:
        f = open('rank.txt','r')
    except:
        f = open('rank.txt','a')
        f.close()
        canvas.create_text(300,150,text='empty',font='Courier 25 bold')
    else:
        user_lst = [line.strip() for line in f.readlines()]
        f.close()
        if len(user_lst) == 0:
            canvas.create_text(300,150,text='empty',font='Courier 25 bold')
            canvas.create_text(480,350,text='Press b to back',font='Courier 15 bold')
        else:
            user_lst.sort(key = lambda x:int(x.split()[1]),reverse=True)
            canvas.create_text(300,40,text='Name\tScore\tLevel\tDifficulty',font='Courier 15 bold')            
            lst_y = 80
            for i in user_lst:
                canvas.create_text(300,lst_y,text=i,font='Courier 15 bold')
                lst_y += 30
    f = open('rank.txt','r')
    user_lst = [line.strip() for line in f.readlines()]
    f.close()
    user_lst.sort(key = lambda x:int(x.split()[1]),reverse=True)
    if len(user_lst) == 0:
        canvas.create_text(300,150,text='empty',font='Courier 25 bold')
        canvas.create_text(480,350,text='Press b to back',font='Courier 15 bold')
        canvas.focus_set()
        canvas.bind('<Key>',rank_key_event)
    else:
        name_lst = []
        for item in user_lst:
            name_lst.append(item.split()[0])  
        dlg = SimpleDialog(canvas,text='which one to choose',buttons=name_lst,default=0,)
        user_index = dlg.go()
        new_name = user_lst[user_index].split()[0]
        user_score = int(user_lst[user_index].split()[1])
        user_level = int(user_lst[user_index].split()[2])
        difficult = user_lst[user_index].split()[3]
        draw_score()
        show_words()

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

def iseated():
    '''
    This function is to jurdje if the snake is eated a food.
    '''
    global foodx,foody,gamescore,k,level
    #jurdge is the food is be eaten
    for k in range(0,3):
        if foodX[k]==snakeX[0] and foodY[k]==snakeY[0]:
            #when eat a food the score plus one
            gamescore+=1
            draw_score()
            return True
            break
 
def play():
    '''
    This function is the main part of the game
    '''
    global new_x,new_y,speed,foodX,foodY
    #main loop only stop when dead
    canvas.delete(ALL)
    draw_wall()
    draw_food()
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
#    gameover()
    success()

def test(event):
    if event.keycode == 84:
        play()

def update_food():
    global foodx,foody,foodX,foodY
    for i in range(0,3):
        random_food()
        foodX[i] = foodx
        foodY[i] = foody

def gameover():
    '''
    This function is to display the information of when dead
    '''
    #delete the items on the canvas and show the score.
    canvas.delete(ALL)
    draw_wall()
    canvas.create_text(300,100,text='Game Over!',font='Verdana 30 bold')
    canvas.create_text(300,200,text='Your score is : '+str(gamescore),font='Verdana 20 bold')
    canvas.create_text(300,275,text='Press R to retry\nN to start a new game \n Q to exit',font='Verdana 15 bold')
    canvas.create_text(400,325,text='Design by DuanYi \nEmail:Duanyi@hit.edu.cn',font='Verdana 10 bold')
    canvas.bind('<Key>',restart)

def restart(event):
    '''
    This function is to restart the game.
    '''
    global gamescore,step,snakeX,snakeY,new_x,new_y,foodx,foody,snakeDirection,level,speed,speed0,foodX,foodY,user_score,difficult,user_lst,new_name,new_item,word_lst,word_lst_random,user_level,user_index
    if event.keycode==81:
        #if user press Q ,exit
        sys.exit()
    if event.keycode==82:
        snakeX=[]
        snakeY=[]
        foodX = [random.randrange(16,571,step)]
        foodY = [random.randrange(16,346,step)]
        foodx=random.randrange(16,571,step)
        foody=random.randrange(16,346,step)
        gamescore = 0
        new_x=16+(3*step)
        new_y=16+(6*step)
        
        for i in range(6,9):
            snakeX.append(16+(3*step))
            snakeY.append(16+(i*step))
        
        for i in range(0,2):
            random_food()
            foodX.append(foodx)
            foodY.append(foody)
        reshow()
        
    if event.keycode==78:
        #delete all the items.
        canvas.delete(ALL)        
        #reset all the variable
        step = 15
        gamescore = 0
        user_score = 0
        user_level = 0
        speed = 0
        speed0 = 0
        level = 1
        user_index = -1
        difficult = ''
        user_lst = []
        new_name = ''
        new_item = []
        word_lst = []
        word_lst_random = []
        snakeX=[]
        snakeY=[]
        foodX = [random.randrange(16,571,step)]
        foodY = [random.randrange(16,346,step)]
        foodx=random.randrange(16,571,step)
        foody=random.randrange(16,346,step)
        
        new_x=16+(3*step)
        new_y=16+(6*step)
        
        for i in range(6,9):
            snakeX.append(16+(3*step))
            snakeY.append(16+(i*step))
        
        for i in range(0,2):
            random_food()
            foodX.append(foodx)
            foodY.append(foody)
        draw_score()
        first_page()

def reshow():
    canvas.delete(ALL)
    draw_wall()
    draw_score()
    lst_y = 80
    for i in word_lst_random:
        canvas.create_text(300,lst_y,text=i,font='Courier 25 bold')
        lst_y += 50
    canvas.create_text(450,350,text='Ready? Press \'T\' to test!',font='Courier 12 bold')
    canvas.focus_set()
    canvas.bind('<Key>',test)        

def success():
    global gamescore,user_score,difficult,user_lst,new_name,new_item,word_lst,word_lst_random,user_level,user_index
    canvas.delete(ALL)
    draw_wall()
    user_score += gamescore
    user_level += 1
    new_item.append(new_name)
    new_item.append(str(user_score))
    new_item.append(str(user_level))
    new_item.append(difficult)
    item = '\t'.join(new_item)       
    f = open('rank.txt','r')
    user_lst = [line.strip() for line in f.readlines()]
    f.close() 
    user_lst.append(item)
    if user_index != -1:
        del user_lst[user_index]
    user_lst.sort(key = lambda x:int(x.split()[1]),reverse=True)
    for i in range(0,len(user_lst)-1):
        user_lst[i] += '\n'    
    f = open('rank.txt','w')
    f.writelines(user_lst)
    f.close()
    canvas.create_text(300,100,text='You Win!',font='Verdana 30 bold')
    canvas.create_text(300,200,text='Your score is : '+str(gamescore),font='Verdana 20 bold')
    canvas.create_text(300,275,text='press N to next game \n Q to exit',font='Verdana 15 bold')
    canvas.focus_set()
    canvas.bind('<Key>',success_event)    

def success_event(event):
    if event.keycode == 81:
        sys.exit()
    if event.keycode == 78:        
        show_words()
        
"=== Main Part ==="
step = 15
gamescore = 0
user_score = 0
user_level = 0
speed = 0
speed0 = 0
level = 1
user_index = -1
difficult = ''
user_lst = []
new_name = ''
new_item = []
word_lst = []
word_lst_random = []
snakeX=[]
snakeY=[]
foodX = [random.randrange(16,571,step)]
foodY = [random.randrange(16,346,step)]
foodx=random.randrange(16,571,step)
foody=random.randrange(16,346,step)

new_x=16+(3*step)
new_y=16+(6*step)

for i in range(6,9):
    snakeX.append(16+(3*step))
    snakeY.append(16+(i*step))

for i in range(0,2):
    random_food()
    foodX.append(foodx)
    foodY.append(foody)
    

snakeDirection = 'DOWN'

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

first_page()

window.mainloop()