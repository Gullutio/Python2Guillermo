# abcdefghijklmnopqrstuvwxyz
# example 1
# input:guillermo, shift 2
# outputk:iwnngtoq
# example 2: zebra, shift 4
# output:difve
# example 3: sus2, shift 26
# output 4:sus2
# make a list with all the letters of the alphabet
# iterate through each letter(chars) in the user input and find it in the list(alph),
# then itereate forward in the list the ammount of shifts(shift) the user types in.
print('Hello')
full = ''
alph = ('abcdefghijklmnopqrstuvwxyz')
input_text = input(
    'put a word here or else... ill be very sad and i will have nothingv to do - ')
shifts = int(input('enter the ammount of chracaters that you want to shift'))
for char in input_text:
    if char in alph:
        char = alph[((alph.index(char)) + shifts) % 26]
    full = full + char

print(full)
