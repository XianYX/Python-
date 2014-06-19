# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Administrator\.spyder2\.temp.py
"""
date = open('111.txt','r')

lst = [i.strip() for i in date.readlines()]

for i in lst:
    lst[lst.index(i)] = i + ' ok\n'
date.close()

print lst
date = open('111.txt','w')
for i in lst:
    date.write(i)

date.close()