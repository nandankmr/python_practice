import datetime
a=input('Enter 1st date (yyyy-mm-dd) ')
d=input('Enter 2nd date (yyyy-mm-dd) ')
b,d=a.split('-'),d.split('-')
c,d=[int(i) for i in b],[int(i) for i in d]
print(datetime.date(d[0],d[1],d[2])-datetime.date(c[0],c[1],c[2]))