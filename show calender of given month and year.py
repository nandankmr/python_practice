import calendar

year = int(input('Enter year:'))
month = int(input('Enter month:'))
a = calendar.monthcalendar(year, month)
for i in a:
    print(i)
