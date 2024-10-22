def unique_chars(word):
    final_u = 0
    u_chars = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'b':0,'w':0,'x':0,'y':0,'x':0}   #hello h = 0____h=1  unique +=1+1+1 e=1 l = 0 l=1 l=1 0=0
    for char in word:
        if char in u_chars:
            if u_chars[char] == 0:
                u_chars[char] += 1
                final_u += 1
    return final_u

input_text = input('please type in a word so I can see how many unique characters there are --> ')
print(f'Your word:"{input_text}" has a grand total of {unique_chars(input_text)} unique characters!')