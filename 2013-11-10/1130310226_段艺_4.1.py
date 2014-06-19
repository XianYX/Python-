# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is the Pig Latin game. 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-11-10 15:54:29
"""
#set the list of vowel and an empty list
vowel1 = ['a','e','i','o','u']
vowel2 = ['a','e','i','o','u','y']
new = []
#let the user to input the string
Str = raw_input()
#make the letter in lowercase and split the string
s = Str.lower()
s = s.split()
#loop the list to do with the words
for i in s:
    #if the str is only one letter
    if len(i) == 1:
        if i in vowel1:
            new_s = i + 'hay'
            new.append(new_s)
        else:
            new_s = i + 'ay'
            new.append(new_s)
    #the first letter is vowel
    elif i[0] in vowel1:
        new_s = i + 'hay'
        new.append(new_s)
    #the first two letters are 'qu'
    elif len(i) >= 2 and i[:2] == 'qu':
        new_s = (i + 'quay')[2:]
        new.append(new_s)
    #the first letter is other letters
    else:
        n = 0
        p = i[1:]
        for j in p :
            if j in vowel2 :
                k = p.index(j) + 1 
                new_s = (i + i[:k] + 'ay')[k:]
                new.append(new_s)
                break
            else:
                n += 1
                if n == len(i) - 1:
                    new_s = i + 'ay'
                    new.append(new_s)
#print the new string
print str(' '.join(new))
            
