import math as m
print('Hello i will calculate the area of a triangle')
s1 = float(input('Values for side 1 '))
s2 = float(input('Values for side 2 '))
s3 = float(input('Values for side 3 '))
s = float(s1 + s2 + s3)
area = m.sqrt(s * s - s1 * s-s2 * s-s3)
print(f'The area of your triangle is {area}.')
