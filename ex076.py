minus = 1
final = ''
input_text = input('type in a word - ')
input_text = input_text.lower()
for char in input_text:
    if char.isalpha() == False:
        input_text = input_text.replace(char, '')
for char in input_text:
    final = final + input_text[len(input_text) - minus]
    minus = minus + 1
if input_text == final:
    print(f'"{input_text}" is a palindrome!')
else:
    print(f'"{input_text}" is not a palindrome!')
