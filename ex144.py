import ex143
def decap(w1, w2):
    r_char = {' ': '', "'":'','.':'',',':'','?':'','!':'',':':'',';':''}
    w1 = w1.lower()
    w2 = w2.lower()
    for char in w1:
        if char in r_char:
            w1 = w1.replace(char, r_char[char])
    for item in w2:
        if item in r_char:
            w2 = w2.replace(item, r_char[item])
    return w1, w2

input_text1 = input('type in your first word to analyze - ')
input_text2 = input('type in your second word to analyze - ')
word1, word2 = decap(input_text1,input_text2)
print(f"WOW! It is {ex143.ana_finder(word1, word2)} that your word is an anagram!")