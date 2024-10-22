print('hi')

val = int(input('please type in a 4 digit number '))

n1 = val % 10
val1 = val // 10
n2 = val1 % 10
val2 = val // 100
n3 = val2 % 10
val3 = val // 1000
n4 = val3 % 10

calc = n1 + n2 + n3 + n4

print(f'{n4} + {n3} + {n2} + {n1} = {calc}')
