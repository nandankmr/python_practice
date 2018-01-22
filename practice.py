def fact(a):
    if(a>0):
        return a*fact(a-1)
    else:
        return 1


print(fact(5))