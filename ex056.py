print('hi!')


input_text = int(
    input('hey pls type in how many minutes of air time u want --- '))
input_text2 = int(input('hey pls type in how many messages u want --- '))

add_air = (input_text - 50) * 0.25
add_text = (input_text2 - 50) * 0.15
subtot = (add_air + add_text + 0.44 + 15) / 5 * 100

print('-' * 90)
print(f'{"Base Charge":<35s} {15:10.2f}$')
print(f'{"Additional Minutes Charge":<35s} {add_text:10.2f}$')
print(f'{"Additional Text Charge":<35s} {add_text:10.2f}$')
print(f'{"911 Fee":<35s} {0.44:10.2f}$')
print(f'{"Tax":<35s} {subtot - (input_text - input_text2 - 0.44 - 15 ):10.2f}$')
print(f'{"Total":<35s} {subtot:10.2f}$')
