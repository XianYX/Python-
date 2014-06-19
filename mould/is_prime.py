# -*- coding: utf-8 -*-
"""
Spyder Editor
python 2.7
This program is a mould to jurdge prime.
It's made by Duan Yi.
Student number:1130310226
E-mail:yumendy@163.com
version:1.0
date:2013-10-16 10:49:40
"""
def prime(n):
    """
    This fuction is to jurdje if the vaule of i is a prime.
    If ture the fuction will return Ture.
    """
    j=int(n**0.5)+1
    m=0
    i=3
    while i<j:
        if n%i==0:
            m+=1
            break
        i+=2
    return m==0