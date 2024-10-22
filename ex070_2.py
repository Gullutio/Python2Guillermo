# Greet the player and ask them for a bit.
# Continue asking the player for bits.
# When they type in a blank space you must tell them the parity bit to their bits.
# If the user did not type in 8 bits display an error message.
input_text = 0
input_text = str(input_text)

print('It is I, the parity bit guy.')
while input_text != '':
    no_ones = 0
    ones = 0
    input_text = input('Type in a parity bit, or else... Type in a space!!!')

    if input_text == '':
        print('Bye! see u latr!')
        break

    if len(input_text) != 8:
        print('invalid')
        continue

    for i in range(len(input_text)):

        if input_text[i] == '1':
            ones = ones + 1

        if input_text[i] != '1' and input_text[i] != '0':
            no_ones = 1
            continue

    if ones % 2 == 0:
        bit = 0

    elif ones % 2 == 1:
        bit = 1

    if no_ones == 1:
        no_ones = 1
        print('invalid')
        continue

    if no_ones != 1:
        print(f'{bit}-{input_text}')
