# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:25:09 2013

@author: Administrator
"""
from Tkinter import *
import random,sys

def draw_wall():
    '''
    This function is to draw the wall.
    '''
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
#    canvas.bind('<Key>',pass)


gamescore=0
level=1

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