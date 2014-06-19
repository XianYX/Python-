# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for proving "Digital black hole"
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-13 12:16:02
"""
#this faction is for counting the number of the odd and even
def count_odd_and_even_number(n):
    n=str(n)
    i=j=0
    for m in range(1,l+1):
        #get the number in the string
        a=int(n[-1*m])
        #jurdge the parity of the number
        if a%2==0:
            #count the number of the odd and even
            j += 1
        else:
            i += 1
    b=str(j)+str(i)
    return b

#input the number which is needed to prove
try:
    n=int(raw_input("please input a integer which is more than 99 : "))
except:
    print("please enter a number!")
else:
    l=len(str(n))
    if l<3:
        print("The integer must more than 99!")
    else:
        #output the result
        while True:
            l=len(str(n))
            m=count_odd_and_even_number(n)+str(l)
            print(m)
            n=int(m)
            if n==123:
                print("BLACK HOLE!")
                break
                
            
    
