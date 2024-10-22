import sys
try:
    words = {}
    word = ''
    print(sys.argv)
    with open(sys.argv[1],'r') as file:
        for line in file:
            processed = line.lower().strip().split()
            for item in processed:
                word = ''
                for letter in item:
                    if letter.isalnum():
                        word += letter

                if word != '':
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1

        print(f'The word "{max(zip(words.values(), words.keys()))[1]}" was repeated a grand total of {max(words.values())} times')
    

except FileNotFoundError:
    print('file couldnt be found')