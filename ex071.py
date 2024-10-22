print('hi')
print('approx1 = 3')
approxes = 1
num1 = 2
num2 = 0
l_result = 3
calcer = 0
for i in range(14):
    approxes = approxes + 1
    num2 = num1 + 1
    num1 = num1 + 1
    if approxes % 2 == 1:
        calcer = ((num1 * num2) * (num2-1))/4 - l_result
        print('-')
        print(num1)
        print(num2)
        print(l_result)
    else:
        calcer = ((num1 * num2) * (num2-1))/4 + l_result
        print('+')
        print(num1)
        print(num2)
        print(l_result)

    print(f'approx{ approxes} = {calcer} ')
    l_result = calcer
