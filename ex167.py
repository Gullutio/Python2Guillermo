import sys

try:    
    if len(sys.argv) < 2:
        print("oops: Missing file name.")
        sys.exit(1)
  
    char_list = [',', ' ', '"', "'", '!', '?', '.','\n']
    inv_words = set()

    with open("words.txt", "r") as words_file:
        word_set = {word.strip().lower() for word in words_file}

   
    with open(sys.argv[1], "r") as user_file:
        for line in user_file:
            word = ''
            for char in line:
                if char not in char_list:
                    word += char
                else:
                    if word: 
                        lower_word = word.lower()
                        if lower_word not in word_set:
                            inv_words.add(lower_word)
                        word = '' 
            if word:
                lower_word = word.lower()
                if lower_word not in word_set:
                    inv_words.add(lower_word)


    if inv_words:
        print("misspelled words:", ", ".join(inv_words))
    else:
        print("no misspelled words found.")

except FileNotFoundError as e:
    print(f"oops: {e}")
   