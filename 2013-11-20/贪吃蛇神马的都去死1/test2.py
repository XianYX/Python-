# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:08:51 2013

@author: Administrator
"""
from Tkinter import *
letter_lst = ['a','b','c','d','e','f','g','h','i''j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
canvas = Canvas(root)

word_order = ''.join(word_lst_random)




i = 0

def now_letters():
    now_letter = []
    now_letter.append(word_order[i])
    now_letter.append(lst[random.range(0,26)])
    now_letter.append(lst[random.range(0,26)])
    
    
def draw_letters():
    for i in range(0,3):
        
        canvas.create_text(foodX[i] + 7,foodY[i] + 7,text = now_letter[i])