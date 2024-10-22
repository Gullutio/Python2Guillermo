# 3.3 = 1.65 ---- 3 = 1.5 ---- 2.7 = 1.35

print('HI')
try:
    input_text = float(
        input('type in the grade number u want me to analyse --->   '))

    if input_text >= 4:
        print('your grade is A+, congrats!!!')

    elif input_text < 4 and input_text >= 3.85:
        print('your grade is A, thats a very good mark')

    elif input_text < 3.85 and input_text >= 3.5:
        print('your grade is A-, thats decent')

    elif input_text < 3.5 and input_text >= 3.15:
        print('your grade is B+, im sure you will do better next time')

    elif input_text < 3.15 and input_text >= 2.85:
        print('your grade is B, you should study more')

    elif input_text < 2.85 and input_text >= 2.5:
        print('your grade is B-, if you dont do better you might fail this subject')

    elif input_text < 2.5 and input_text >= 2.15:
        print('your grade is C+, thats a bad grade')

    elif input_text < 2.15 and input_text >= 1.85:
        print('your grade is C, thats a very bad grade ')

    elif input_text < 1.85 and input_text >= 1.5:
        print('your grade is C-, you should feel an urge to study more')

    elif input_text < 1.5 and input_text >= 1:
        print('your grade is D+, you are not studying enough')

    elif input_text < 1 and input_text >= 0.5:
        print('your grade is D, oh no!')

    elif input_text < 0.5:
        print('your grade is F, Ok man, lock in')

    else:
        print('not a valid value')


except:
    print('not a valid value')
