a=600851475143
b=600851475143
while a>0:
    if(b%a==0):
        c=1
        d=0
        while c<=a:
            if(a%c==0):
                d+=1
            c+=1
        if(d==2):
            break
    a-=1
print (a)
