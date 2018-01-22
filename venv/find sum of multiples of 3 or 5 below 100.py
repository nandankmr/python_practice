a=1
b=0
while a<1000:
    if(a%3==0 or a%5==0):
        b=b+a
    a=a+1
else:
    print (b)