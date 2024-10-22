try:
    longest_word = []
    max_len = 0
    with open('ex150.txt', 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_len = len(word)
                if word_len > max_len:
                    max_len = word_len
                    longest_word = [word]
                elif word_len == max_len:
                    longest_word.append(word)
    print(f'Length: {max_len}, Word: {longest_word}')

except FileNotFoundError:
    print('sorry there was an error with your file')