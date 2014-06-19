# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is for estimating pi 
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.1
date:2013-10-11 17:59:33
"""
#import the necessary function
from math import sqrt
from math import fabs
from math import factorial
#set the original value
pi1=0
k=term=0
a=(2*sqrt(2)/9801)
#computing pi
while True:
    b=factorial(4*k)*(1103+26390*k)
    c=((factorial(k))**4)*(396**(4*k))
    term=a*b/c
    if fabs(term)<1e-15 :break
    pi1 += term
    k += 1
#output the result
print(1/pi1)    
