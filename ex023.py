import math as m
print('I am polygon maker')
s = float(input('What do you want the length of my sides to be.'))
n = float(input('How many sides do you want me to have.'))
area = (n * s * s) / 4 * m.tan(m.pi/n)
print(f'The area of your polygon is {area:.0f}.')
