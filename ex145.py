def scrabble_score(word):
    word = word.lower()
    final_score = 0
    scorer = {'a':1,'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1, 'd':2,'g':2, 'bcmp':3,'c':3,'m':3,'p':3, 'f':4,'h':4,'v':4,'w':4,'y':4,'k':5, 'j':8,'x':8, 'q':10,'z':10}
    for item in word:
        if item in scorer:
            final_score += scorer[item]
    return final_score

input_text = input('please type in a word - ')
print(scrabble_score(input_text))