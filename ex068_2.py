print('Hello')
grades = 0
num_grades = 0
sum = 0
try:

    while grades != '':
        grades = input('gimme grades')
        num_grades = num_grades + 1

        if grades == 'A+':
            sum = sum + 4

        elif grades == 'A':
            sum = sum + 4

        elif grades == 'A-':
            sum = sum + 3.7

        elif grades == 'B+':
            sum = sum + 3.3

        elif grades == 'B':
            sum = sum + 3

        elif grades == 'B-':
            sum = sum + 2.7

        elif grades == 'C+':
            sum = sum + 2.3

        elif grades == 'C':
            sum = sum + 2

        elif grades == 'C-':
            sum = sum + 1.7

        elif grades == 'D+':
            sum = sum + 1.3

        elif grades == 'D':
            sum = sum + 1

    print(f'your average is {sum / (num_grades - 1)} / 4.')
except:
    print('0')
