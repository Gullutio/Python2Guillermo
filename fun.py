import time as t
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print('Hello, welcome to...')
for i in range(3):
    t.sleep(0.5)
    print('.')
print('Where are we?')
t.sleep(1)
print('Anyways!!!')
t.sleep(0.2)

input_text = input('Mind telling me a joke!? - ')
full = ''
calcer = 0
c1 = 0
fuller = ''

for i in range(len(input_text)):
    c1 = c1 + 1
    calcer = len(input_text) - c1
    database = input_text[calcer]
    full = full + database

print(f'Heres my joke!!! {full}')

t.sleep(2)
print('So?')
t.sleep(0.2)
print('DID')
t.sleep(0.2)
print('YOU')
t.sleep(0.2)
print('like it???')

for i in range(3):
    t.sleep(0.5)
    print('.')
name = input('What IS your name?')
for char in name:
    if char in alph:
        char = alph[((alph.index(char)) + 5) % 26]
    fuller = fuller + char

t.sleep(0.5)
print(f'Ok,{name}.')
t.sleep(0.5)
print(f'{name}, how did you get here anyways?')
t.sleep(2)
print('Meh, who cares.')
t.sleep(0.5)
print(f'the important thing is that you are here now, {name} :)')
t.sleep(2)
print(f'Not gonna lie, {name} is kinda hard for me to pronounce.')
t.sleep(0.7)
print(f'Could I call you {fuller}?')

for i in range(3):
    t.sleep(0.5)
    print('?')

t.sleep(1)
print(f'Ill take that as a yes, {fuller}...')
t.sleep(1)
print('What?')
t.sleep(1)
print('Did you hear that?')

for i in range(10):
    t.sleep(0.2)
    print('HihihihawHihihihawHihihihawHihihihaw')

t.sleep(1)
print('Sorry did I talk to loudly?')
t.sleep(1)
print('It sometimes happens')
t.sleep(3)

try:
    while merit == 1:
        input_text = float(
            input('In numbers, what was your grade this year -  '))

        if input_text >= 4:
            print('your grade is A+, congrats!!!')

        elif input_text < 4 and input_text >= 3.85:
            print('your grade is A, thats a very good mark')

        elif input_text < 3.85 and input_text >= 3.5:
            print('your grade is A-, thats decent')

        elif input_text < 3.5 and input_text >= 3.15:
            print('your grade is B+, im sure you will do better next time')

        elif input_text < 3.15 and input_text >= 2.85:
            print('your grade is B, you should study more')

        elif input_text < 2.85 and input_text >= 2.5:
            print('your grade is B-, if you dont do better you might fail this subject')

        elif input_text < 2.5 and input_text >= 2.15:
            print('your grade is C+, thats a bad grade no food for 10 days')

        elif input_text < 2.15 and input_text >= 1.85:
            print('your grade is C, thats a very bad grade get out of my house+')

        elif input_text < 1.85 and input_text >= 1.5:
            print('your grade is C-, you should feel ashamed for yourself')

        elif input_text < 1.5 and input_text >= 1:
            print('your grade is D+, you are living trash')

        elif input_text < 1 and input_text >= 0.5:
            print('your grade is D, your brain is as small as a pea')

        elif input_text < 0.5:
            print('your grade is F, You will get expelled soon.')

        else:
            print("Huh, what's that?")
            merit = 1


except:
    print('Speak more clearly.')
    merit = 1