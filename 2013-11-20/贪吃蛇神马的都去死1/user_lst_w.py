# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:19:30 2013

@author: Administrator
"""
f = open('rank.txt','r')
lst = [line.strip() for line in f.readlines()]
f.close()



lst.sort(key = lambda x:int(x.split()[1]),reverse=True)

for i in range(0,len(lst)-1):
    lst[i] += '\n'
f = open('rank.txt','w')
f.writelines(lst)
f.close()
