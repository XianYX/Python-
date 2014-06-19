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
"=== Model Part ==="


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
    global difficult,speed,show_time,word_lst,word_lst_random
    if event.keycode == 66:
        canvas.delete(ALL)
        first_page()
    elif event.keycode == 69:
        difficult = 'easy'
        speed = 200
        show_words()
    elif event.keycode == 77:
        difficult = 'middle'
        speed = 150
        show_words()
    elif event.keycode == 72:
        difficult = 'hard'
        speed = 100
        show_words()

def show_words():
    canvas.delete(ALL)
    draw_wall()
    global difficult
    if difficult == 'easy':
        f = open('easy1671.txt','r')
        word_lst = [line.strip() for line in f.readlines()]
        f.close()
        for i in range(0,3):
            random_word = word_lst[random.randrange(0,1672)]
            word_lst_random.append(random_word)
    elif difficult =='middle':
        f = open('middle2104.txt','r')
        word_lst = [line.strip() for line in f.readlines()]
        f.close()
        for i in range(0,4):
            random_word = word_lst[random.randrange(0,2105)]
            word_lst_random.append(random_word)
    elif difficult == 'hard':
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

def load():
    global new_name,difficult,level,game_score
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
        game_score = user_lst[user_index].split()[1]
        level = user_lst[user_index].split()[2]
        difficult = user_lst[user_index].split()[3]
        show_words()
 
def play():
    canvas.delete(ALL)
    draw_wall()
    print 'play'
    pass

def test(event):
    if event.keycode == 84:
        play()
            
"=== Main Part ==="

gamescore = 0
speed = 0
level=1
difficult = ''
user_lst = []
new_name = ''
new_item = []
word_lst = []
word_lst_random = []

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
