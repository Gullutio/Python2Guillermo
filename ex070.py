# Greet the player and ask them for a bit.
# Continue asking the player for bits.
# When they type in a blank space you must tell them the parity bit to their bits.
# If the user did not type in 8 bits display an error message.
input_text = 0
input_text = str(input_text)

print('It is I, the parity bit guy.')
while input_text != '':
    index = 0
    ones = 0
    input_text = input('Type in a parity bit, or else... Type in a space!!!')
    for i in range(8):
        input_text[index]
        print(f'{input_text}---15')
        print(f'{index}---16')
        print(f'{ones}---17')
        index = index + 1
        print(f'{input_text}---19')
        print(f'{index}---20')
        print(f'{ones}---21')
        if input_text == 1:
            print(f'{input_text}---23')
            print(f'{index}---24')
            print(f'{ones}---25')
            ones = ones + 1
        print(f'{input_text}---27')
        print(f'{index}---28')
        print(f'{ones}---29')
    if ones % 2 == 0:
        bit = 0

    else:
        bit = 1

print(bit)
