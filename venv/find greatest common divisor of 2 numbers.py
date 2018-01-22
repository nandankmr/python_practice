a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=1
d=0
while c<=a and c<=b:
    if a%c==0 and b%c==0:
        d=c
    c+=1
print(d)
