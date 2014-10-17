# -*- coding: utf-8 -*-
model = raw_input()
flag = 1
k = 273.15
try:
    origin = float(raw_input())
except:
    flag = 0
else:
    if model == '1':
        result = (origin - 32) * 5 / 9 + k
        if result > 0:
            result -= k
        else:
            flag = 0
    elif model == '2':
        result += k
        if result > 0:
            result = 9 * (result - k) / 5 + 32
        else:
            flag = 0
    else:
        flag = 0
    if flag:
       print(str(format(result,'.2f')))
    else:
        print("Error")