def f(n):
"""
this fucation is to computer the factorial
"""
try:
    n=int(n)
    if n<0:
        print("error")
    elif n==0:
        return 1
    else:
        result=n*f(n-1)
        return result
except:
    print("error")

