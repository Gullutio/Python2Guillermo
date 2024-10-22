def text_messenger(text):
    result = ''
    symbols = {'1':'.,?!:','2':'ABC', '3': 'DEF', '4':'GHI', '5':'JKL', '6':'MNQ', '7':'PQRS','8':'TUV', '9':'WXYZ', '10': ' '}
    for char in text.upper():
        for key, value in symbols.items():
            if char in value:
                result += key * (value.index(char) + 1)
    return result


input_text = input('please type in the word you want me to translate')
print(text_messenger(input_text))