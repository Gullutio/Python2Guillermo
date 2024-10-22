print('HI')

try:
    input_text = float(input(
        'hello what rating do you give your employee so i can calculate his raise ---> '))

    calc = input_text * 2400.00

    # if input_text < 0.4 and input_text >= 0:
    if 0 <= input_text < 0.4:
        print('Unnaceptable performance')
        print(f'his raise would be {calc}$')

    # elif input_text < 0.6 and input_text >= 0.40:2
    elif 0.4 <= input_text < 0.6:
        print('Acceptable performance')
        print(f'his raise would be {calc}$')

    elif input_text >= 0.6:
        print('Meritorious performance')
        print(f'his raise would be {calc}$')


except:
    print('not a valid value')
