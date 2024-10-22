print('Hello')
grades = 0
n_g = 0
a2 = 0
a = 0
b2 = 0
b = 0
b3 = 0
c = 0
c3 = 0
d2 = 0
d = 0
c2 = 0
a3 = 0

while grades != '':
    grades = input('gimme grades')
    if grades == 'C+':
        n_g = n_g + 1
        c2 = c2 + 2.3

    elif grades == 'A+':
        n_g = n_g + 1
        a = a + 4

    elif grades == 'A':
        n_g = n_g + 1
        a2 = a2 + 4

    elif grades == 'B+':
        n_g = n_g + 1
        b2 = b2 + 3.3

    elif grades == 'B':
        n_g = n_g + 1
        b = b + 3

    elif grades == 'B-':
        n_g = n_g + 1
        b3 = b3 + 2.7

    elif grades == 'C':
        n_g = n_g + 1
        c2 = c2 + 2

    elif grades == 'C-':
        n_g = n_g + 1
        c3 = c3 + 1.7

    elif grades == 'D+':
        n_g = n_g + 1
        d2 = d2 + 1.3

    elif grades == 'D':
        n_g = n_g + 1
        d = d + 1

    elif grades == 'A-':
        n_g = n_g + 1
        a3 = a3 + 3.7


print(f'your average is {(a+a2+a3+b+b2+b3+c+c2+c3+d+d2 ) / n_g} / 4.')
