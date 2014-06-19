# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:48:35 2013

@author: Administrator
"""
f = open('middle2104.txt','r')
lst = [line.strip().lower() for line in f.readlines()]
f.close()
#lst.sort(key = lambda x:len(x),reverse=False)
for i in range(0,len(lst)-1):
    lst[i] += '\n'
f = open('middle2104.txt','w')
f.writelines(lst)
f.close()
