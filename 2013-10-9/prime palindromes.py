# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for picking the Prime palindromes.
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-16 10:55:43
"""
#define the faction for jurdge prime 
"""
This fuction is to jurdje if the vaule of i is a prime.
If ture the fuction will return Ture.
"""

def prime(n):
    j=int(n**0.5)+1
    m=0
    i=3
    while i<j:
        if n%i==0:
            m+=1
            break
        i+=2
    return m==0
    
"""
This fuction is to turn the number
"""
def turn(n):
    m=str(n)    
    tn=int(m[::-1])
    return tn

#set the start of the number 
n=11
#main part
#set the times of loop 
while n<100000:
    #select the prime
    if int(str(n)[0])%2!=0:
        if prime(n)==True:        
            #turn the number
            tn=turn(n)
            #jurdge if the turn number is prime
            if prime(tn)==True:
                #print the result
                print(n)            
    n+=2    
