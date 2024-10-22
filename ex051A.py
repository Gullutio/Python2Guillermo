# use a dictionary so that it checks the users input and puts the grade

print('HI')
try:
    input_text = input('type in the grade u want me to analyse').title()
    grades = {'A+': 4, 'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3, 'B-': 2.7,
              'C+': 2.3, 'C': 2, 'C-': 1.7, 'D+': 1.3, 'D': 1, 'F': 0}

    print(f'Your grade is {grades[input_text]}')
except:
    print('not a valid value')
