print('        Hello I am eartqauke bot please type in the magnituse of the earthqauke you wnat me to analyse, thank you for using this program and trustng us with our earthquake magnitude meter')


try:
    input_text = float
    (input(
        'Please type in the magnitude of your earthquake here, thanks!!!'))

    if input_text < 2 and input_text >= 0:
        print('Thats a Micro Earthquake')

    elif input_text < 3 and input_text >= 2:
        print('That is a Very minor earthquake')

    elif input_text < 4 and input_text >= 3:
        print('That is a minor earthquake')

    elif input_text < 5 and input_text >= 4:
        print('That is a light earthquake')

    elif input_text < 6 and input_text >= 5:
        print('That is a moderate earthquake')

    elif input_text < 7 and input_text >= 6:
        print('That is a strong earthquake')

    elif input_text < 8 and input_text >= 7:
        print('That is a Major earthquake')

    elif input_text < 10 and input_text >= 8:
        print('That is a Great earthquake')

    elif input_text >= 10:
        print('That is a Meteoric earthquake')

    else:
        print('Sorry that is not a valid value')

except:
    print('Sorry that is not a valid value')
