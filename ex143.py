def ana_finder(word1,word2): 
    isana = True  
    chars = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'b':0,'w':0,'x':0,'y':0,'x':0}

    for letter in word1:
        if letter in chars:
            chars[letter] += 1

    for item in word2:
        if item in chars:
            chars[item] -= 1

    for i in chars:
        if chars[i] != 0:
            isana = False

    return isana

if __name__ == "__main__":            
    input_text1 = input('type in your first word to analyze - ')
    input_text2 = input('type in your second word to analyze - ')
    print(f"WOW! It is {ana_finder(input_text1, input_text2)} that your word is an anagram!")