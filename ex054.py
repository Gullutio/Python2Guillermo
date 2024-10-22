print('Hello')

try:
    input_text = float(input('Please type in a value'))

    if input_text < 380:
        print('Thats not a valid value')

    elif input_text < 450:
        print('wavelength = violet')

    elif input_text < 495:
        print('wavelength = blue')

    elif input_text < 570:
        print('wavelength = green')

    elif input_text < 590:
        print('wavelength = yellow')

    elif input_text < 620:
        print('wavelength = orange')

    elif input_text < 750:
        print('wavelength = red')

    else:
        print('Thats not a valid value')

except:
    print('thats not a valid value')
