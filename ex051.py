print('what was ur last exams note')
input_text = input(
    'please type in the grade u want me to analyse. --->').title()

try:
    if input_text == 'A+':
        print('You have 4 points')

    elif input_text == 'A':
        print('You have 4 points')

    elif input_text == 'A-':
        print('You have 3.7 points')

    elif input_text == 'B+':
        print('You have 3.3 points')

    elif input_text == 'B':
        print('You have 3 points')

    elif input_text == 'B-':
        print('You have 2.7 points')

    elif input_text == 'C+':
        print('You have 2.3 points')

    elif input_text == 'C':
        print('You have 2.0 points')

    elif input_text == 'C-':
        print('You have 1.7 points')

    elif input_text == 'D+':
        print('You have 1.3 points')

    elif input_text == 'D':
        print('You have 1 points')

    elif input_text == 'F':
        print('You have 0 points')

    else:
        print('Sorry that is not a valid value')

except:
    print('Sorry that is not a valid value')
