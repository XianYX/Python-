def f(n):
    """
    this fucation is to computer the sum
    """
    try:
        n=int(n)
        if n<0:
            print("error")
        elif n==1:
            return 1
        else:
            result=n+f(n-1)
            return result
    except:
        print("error")
    
print f(100)