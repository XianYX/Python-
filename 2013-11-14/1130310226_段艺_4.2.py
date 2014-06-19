# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is the Pig Latin game. 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-11-14 21:51:03
"""
#import the re model
import re
#set an empty list
new = []
#make the words lower
s = raw_input().lower()
s = s.split()
#set thr re rule
m1 = re.compile(r'([aeiou])(\w*)')
m2 = re.compile(r'(qu)(\w*)')
m3 = re.compile(r'([aeiouy])(\w*)\b')
#change the word
for i in s:
    if re.match(m1,i):
        new.append(re.match(m1,i).group(0) + 'hay')
    elif re.match(m2,i):
        new.append((re.match(m2,i).group(0) + 'quay')[2:])
    elif re.search(m3,i[1:]):
        k = re.search(m3,i[1:]).start(0) + 1
        new.append((i + i[:k] + 'ay')[k:])
    else :
        new.append(i + 'ay')
#print the new string
print str(' '.join(new))
            
