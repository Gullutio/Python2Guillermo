print('hello')
input = 3
num1 = 2
num2 = 3
num3 = 4
rot_num = 1
approxes = 1

print(f'1 = {input}')
input = 3+(4/(num1*num2*num3))
print(f'{rot_num+1}={input}')

for i in range(13):
    rot_num = rot_num + 1
    approxes = approxes + 1

    if approxes % 2 == 1:
        num1 = num1+2
        num2 = num2+2
        num3 = num3+2
        input = input+(4/(num1*num2*num3))
        print(f'{rot_num+1}={input}')

    else:
        num1 = num1+2
        num2 = num2+2
        num3 = num3+2
        input = input-(4/(num1*num2*num3))
        print(f'{rot_num+1}={input}')
