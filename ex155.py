try:
    words = {}
    word = ''
    input_text = input('please type in your file - ')
    with open(input_text,'r') as file:
        for line in file:
            processed = line.strip().split()
            for item in processed:
                word = ''
                for letter in item:
                    if letter.isalnum():
                        word += letter.lower()

                if word != '':
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
        max_words = max(words.values())
        max_key = max(zip(words.values(), words.keys()))[1]
        print(f'The word "{max_key}" was repeated a grand total of {max_words} times in the file {input_text}')
    

except FileNotFoundError:
    print('file couldnt be found')