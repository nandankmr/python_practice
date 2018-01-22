#!usr/bin/python
a=int(input('Enter a number:'))
b=1
c=0
while b<=a:
    if a%b==0:
        c=c+1
    b=b+1
if c==2:
    print('Number is prime')
else:
    print('Number is not prime')
