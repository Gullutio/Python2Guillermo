import sys
import ex117
try:
    word_count = {}
    print(sys.argv)
    with open(sys.argv[1],'r') as file:
        for line in file:
            words = ex117.word_findr(line)
            #words[-1] = words[-1].rstrip('\n')
            for word in words:
                word = word.lower().strip('\n')
                if word != '':
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        print(f'The word "{max(zip(word_count.values(), word_count.keys()))[1]}" was repeated a grand total of {max(word_count.values())} times')
    

except FileNotFoundError:
    print('file couldnt be found')