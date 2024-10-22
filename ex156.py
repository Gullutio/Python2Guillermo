input_text = ' '
sum = 0

while input_text != '':      
    try:
            input_text = input('type in number')
            sum += int(input_text)
            print(sum)
    except:
        if input_text != '':
            print('please type in a valid number next time!')
            continue