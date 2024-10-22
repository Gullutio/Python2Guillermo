print('Hi')
input_text = float(input('PLease type in a value ---> '))

try:

    if input_text < 3e9:
        print('Those are radio waves')

    elif 3e9 <= input_text < 3e12:
        print('Those are microwaves')

    elif input_text < 4.3e14:
        print('Those are infrared lights')

    elif input_text < 7.5e14:
        print('Those are Visible light')

    elif input_text < 3e17:
        print('THose are Ultraviolet lights')

    elif input_text < 3e19:
        print('Those are Xrays')

    elif 3e19 <= input_text:
        print('Those are gamma rays')

    else:
        print('Sorry thats not a valid value.')


except:
    print('Sorry that is not a valid value')
