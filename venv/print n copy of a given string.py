a=input('Enter a string:')
b=int(input('Enter nunber of times:'))

for n in range(0,b):
    if len(a) >= 2:
        print(a[0],a[1])
    else:
        print(a)
