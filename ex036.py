print('Hello I am consonant and vowel bot.')
cw = input('Hi please type in the letter you want me to analyse.Thanks! ')

if cw == 'y':
    print('y can be a consonant or a vowel')

elif cw == 'a' or cw == 'e' or cw == 'i' or cw == 'o' or cw == 'u':
    print("that's a vowel")

elif len(cw) > 1 or not cw.isalpha():
    print("that's not a letter dummy")

else:
    print("that's a consonant")
