def tokenizer(input_text):
    lastnum = False
    tokens = []

    for char in input_text:
        if char.isnumeric():
            if lastnum == True:
                tokens[-1] += char
            else:
                tokens.append(char)
                lastnum = True
        elif char in '*/^+-':
            lastnum = False
            tokens.append(char)
            
    return tokens

if __name__ == "__main__":
    input_text = input('type in a mathematical expression for me to tokenize --- ')
    print(tokenizer(input_text))