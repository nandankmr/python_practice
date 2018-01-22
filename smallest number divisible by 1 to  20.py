a=1
while (a):
    i=1
    j=0
    while i<=17:
        if a%i!=0:
            j+=1
        i+=1
    if j==0:
        break
    a+=1
print (a)

