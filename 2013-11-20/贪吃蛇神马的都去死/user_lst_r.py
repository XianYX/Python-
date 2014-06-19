# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Administrator\.spyder2\.temp.py
"""
try:
    f = open('rank.txt','r')
except:
    f = open('rank.txt','a')
    f.close()
else:
    user_lst = [line.strip() for line in f.readlines()]
    f.close()