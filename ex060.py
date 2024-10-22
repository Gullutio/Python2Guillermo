# 0 - 37 randint

from random import randint

spin_res = randint(0, 37)
color = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


if spin_res == 0:
    print('Pay 0')
    quit()

if spin_res == 37:
    print('Pay 00')
    quit()

if spin_res in color:
    color = 'Red'


else:
    color = 'Black'


if spin_res % 2 == 0:
    ev_odd = 'Even'

else:
    ev_odd = 'Odd'


if spin_res >= 1 and spin_res <= 18:
    between = '1 and 18'


else:
    between = '19 and 36'


print(f'Pay {spin_res}')
print(f'Pay{color}')
print(f'Pay{ev_odd}')
print(f'Pay{between}')
