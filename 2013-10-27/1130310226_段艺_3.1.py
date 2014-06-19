# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for GUI.
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-27 16:23:36
"""
#import the necessary modle
from Tkinter import *
from tkFont import *
#define function which will be used
def Rectangle():
    '''
    This fuction is to draw a rad rectangle and clean the canvas
    '''
    root.title('Ex3.1.2')
    canvas.delete('Str')
    global Text
    Text=''
    t.set('Mouse Event')
    canvas.create_rectangle(150,100,250,200,fill='red',tags='rectangle')

def keyboard(event):
    '''
    This fuction is to print what you input on canvas and clean the canvas before you input.
    '''
    root.title('Ex3.1.3')
    canvas.delete('rectangle')
    t.set('Keyboard Event')
    ft=Font(size=15,weight=BOLD)
    global Text
    Text+=event.char
    canvas.delete('Str')
    canvas.create_text(200,150,text=Text,font=ft,tags='Str')

def BK(event):
    '''
    This fuction is to delete the last letter which you input.
    '''
    root.title('Ex3.1.3')
    canvas.delete('rectangle')
    t.set('Keyboard Event')
    ft=Font(size=15,weight=BOLD)
    global Text
    Text=Text[0:len(Text)-1]
    canvas.delete('Str')
    canvas.create_text(200,150,text=Text,font=ft,tags='Str')   
#set the main window
root=Tk()
#set the title of the window
root.title('Ex3.1.1')
#define the global variable 'Text'
Text=''
#set the text in lable and print the label on the screen
t=StringVar()
t.set('GUI widgets')
label1=Label(root,textvariable =t)
#set a canvas 
canvas=Canvas(root,bg='white',width=400,height=300)
#set a button which is to draw a red rectangle
button1=Button(root,text='Rectangle',command=Rectangle)
#focus the keyboard event
canvas.focus_set()
canvas.bind("<Key>",keyboard)
canvas.bind("<BackSpace>",BK)
#pack the widget
label1.pack()
canvas.pack()
button1.pack()
#enable the window 
root.mainloop()