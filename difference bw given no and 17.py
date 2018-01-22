# if input is greater than 17 then returns double and absolute value
a = int(input('Enter a number:'))
b = 17 - a
if b < 0:
    b = abs(b) * 2
print(b)
