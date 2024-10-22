print('Hi I am note bot')
print(':))))))))))))))')
input_text = input('please type in the note you want ME to analyse: ').title()
note = input_text[0]
octave = int(input_text[1])
notes = {'C': 261.63, 'D': 293.66, 'E': 329.63,
         'F': 349.23, 'G': 392.00, 'A': 440.00, 'B': 493.880}

result = notes[note] / 2 ** (4 - octave)
print(f'the frequency is {result}')
