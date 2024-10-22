# 1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizz-buzz 16 17 fizz 19 buzz
# start by 1, check if it can be divisible by 3 and 5, if yes print fizz-buzz
# check if it can be divisable by 3 if yes print fizz
# check if it can be divisable by  5 if yes print buzz
# repeat 100 times
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizz-buzz')

    elif i % 3 == 0:
        print('fizz')

    elif i % 5 == 0:
        print('buzz')

    else:
        print(i)
