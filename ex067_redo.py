from math import sqrt

total = 0
res = 0

print('Hi')
try:
    x = float(input('Type first x value'))
    y = float(input('Type first y value'))
    f_x = float(x)
    f_y = float(y)
    x2 = input('Type in next x value')

    while x2 != '':
        y2 = float(input('Type in next y value'))
        x2 = float(x2)
        res = sqrt((x - x2)**2 + (y - y2)**2)
        total = total + res
        x = float(x2)
        y = float(y2)
        x2 = input('Type in next x value')

    res = sqrt((f_x - x)**2 + (f_y - y)**2)
    total = total + res
except:
    print('Wrong value')

print(total)
