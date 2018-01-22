list=[int(x) for x in input('Enter integers separated by space: ').split(' ')]
for item in list:
    j=''
    for i in range(item):
        j+= "*"
    print(j)