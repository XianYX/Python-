# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for picking the Circular primes.
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-16 22:20:32
"""
def prime(n):
    """
    This fuction is to jurdje if the vaule of i is a prime.
    If ture the fuction will return Ture.
    """
    j=int(n**0.5)
    m=0
    i=3
    while i<j:
        if n%i==0:
            m+=1
            break
        i+=2
    return m==0

def prime_loop(n):
    """
    This fuction is to loop the number in the prime
    """
    s=n[1:]+n[0]
    return int(s)
#set the value of the sum and n
sum=0
n=11
#set the time of loop
while n<1000000:
    #jurdje if 2\4\6\8\0\5 are in the number if so skip the number
    m=str(n)
    q="2" not in m and "4" not in m and "6" not in m and "8" not in m and "5" not in m and "0" not in m
    if q==True:
        #jurdge if n is a prime
       if prime(n)==True:
           l=len(m)
           i=1
           #loop the number and jurdge if the number is a perime
           while i<l:
               s=prime_loop(m)
               if prime(s)==False:
                   break
               else:
                   m=str(s)
                   i+=1
           if i==l:
               #count the number
               sum+=1
    n+=2
#output the result
print(sum+4)