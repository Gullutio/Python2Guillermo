# accept a 8 character input from the user that is only composed of 1 and 0.
# Check if the input entered by the user is valid by seeing if it has 8 characters and if it only has 1s and 0s .
# GIve either an error message if the input entered by the user is not 8 characters long or if it is not composed of
# 1s and 0s. or a parity bit after all the code is run annd the code is 8 chars long and it is only 1s and 0s.
# Check if then user enters a space, if yes, end the program and if no rerun it

while True:
    input_text = input('Type in a 8 bit sequence --- ')
    ones = input_text.count('1')
    zeros = input_text.count('0')

    if input_text == '':
        break

    if ones + zeros != 8 or len(input_text) != 8:
        print('invalid value')

    else:
        # if ones % 2 == 0:
        #     bit = 0
        # else:
        #     bit = 1

        bit = 0 if ones % 2 == 0 else 1
        print(f'{bit}-{input_text}')
