a=1
b=2
c=0
while b<4000000:
   # print (a)
    #print (b)

    if a%2==0:
            print(a)
            c=c+a
    if b%2==0:
            print (b)
            c=c+b
    a=a+b
    b=a+b
else:
    print (c)
