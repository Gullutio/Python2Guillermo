

print('Hi i am an averaging bot')
print('Feed me with inputs, when you type the input 0 it means youre done...')

try:
    input_text = 1
    times = 0
    sum = 0

    while input_text != 0:
        input_text = float(input('Please type in a value!'))
        sum = float(input_text + sum)
        times = times + 1

    print(f'your average number is {sum/(times - 1)}')

except:
    print('bad value')
