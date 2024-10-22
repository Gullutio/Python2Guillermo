grades = {'A+':4, 'A':3.85, 'A-':3.5, 'B+':3.15, 'B':2.85, 'B-':2.5, 'C+':2.15, 'C':1.85, 'C-':1.5, 'D+':1, 'D':0.5}
input_text = ' '

def grade_to_letter(input_text, grades):
    if float(input_text) < 0.5:
        print('Thats an F')
    elif float(input_text) >= 4:
        print('Thats an A+')
    else:
        for letter, cutoff in grades.items():
            if float(input_text) >= cutoff:    #<---- converts number grade to letter grade
                print(f'Thats an {letter}')
                break

def letter_to_grade(input_text, grades):
    
    input_text = input_text.strip().upper()
    if input_text in grades:
        print(f'Thats {grades[input_text]} points') #<----- converts letter grade to number grade
    elif input_text == 'F':
        print("Thats 0.5 grade points")
    elif input_text != '':
        print('Invalid')

while input_text != '':
    try:
        input_text = input('type in a grade pls - ')
        grade_to_letter(input_text, grades) 

    except ValueError:
        try:
            letter_to_grade(input_text, grades)
        except:
            print('Invalid grade input')
            continue

