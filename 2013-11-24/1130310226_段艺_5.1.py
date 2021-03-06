# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is Inverted index.
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-11-23 00:53:46
"""
#define the list and dictionary will be used
dic = {}
keys = []
del_lst = []
for_rank = []
#define a function to jurdge if the key words are in dictionary.
def all_in(key_str,dic):
    key_lst = key_str.split()
    for key in key_lst:
        if key not in dic:
            return False
    return True
#input the strings and create the dictionary
for num in range (0,100):
    Str = raw_input()
    temp_lst = Str.split()
    for word in temp_lst:
        if word in dic:
            dic[word].add(num+1)
        else:
            item = set()
            item.add(num+1)
            dic[word] = item
#print the dic
sum_lst = dic.items()
sum_lst.sort(key = lambda x:x[0])
for item in sum_lst:
    line = list(item[1])
    line.sort()
    for i in range(0,len(line)):
        line[i] = str(line[i])
    print item[0] + ':',', '.join(line)
#input the index        
while True:
    key_str = raw_input()
    if key_str == '':
        break
    else:
        keys.append(key_str)
#do with the key words
for key_str in keys:
    if all_in(key_str,dic) == False:
        print 'None'
    #save all the number of line in a list
    else:
        key_lst = key_str.split()
        sum_set = set()
        for k in key_lst:
            sum_set = sum_set | dic[k]
        for k in key_lst:
            sum_set = sum_set & dic[k]
        if len(sum_set) == 0:
            print 'None'
        else:
            lst = list(sum_set)
            lst.sort()
            for i in range(len(lst)):
                lst[i] = str(lst[i])
            print ', '.join(lst)