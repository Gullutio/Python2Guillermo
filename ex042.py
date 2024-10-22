from pickletools import float8


print('Hello i am freq to note bot')
input_text = float(input('What frequency do u want me to analyse?'))
frequencies = {261.63: 'C4', 293.66: 'D4', 329.63: 'E4',
               349.23: 'F4', 440.00: 'A4', 493.88: 'B4'}
print(f'Your note is {frequencies[input_text]}')
