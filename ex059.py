# User enters a value
# We get the vbalue and then we check if it matches any of the characters inn the list
# If there are 3 letters and in the second part aka the numbers there are 3 it is an old liscense plate
# If there are 4 letters and in the second part aka the numbers there are 3 it is an news liscense plate
# Old plates - ZSU313, SUI222
# New plates - 2334SUS, 6767LOL
# see how many letters it has and if they are capitalized, then i have to see how many numbers it has and see if they are in the correct order
# Check if it goes in these orders :  check with isalpha() if the first 3 letters are in the alphabet and then check with isdigit if it is number.  The other possibility is to check if the first 4 characters are numbers and the last 3 characters are letters


print('hi')
input_text = str(input(
    'Please type in a liscence plate. ex: SUS010 Or 2340LOL --->  '))
try:
    old_first = input_text[0: 3].upper()
    old_last = input_text[3:6]
    new_first = input_text[0:4]
    new_last = input_text[4:7].upper()

    if old_first.isalpha() and old_last.isdigit():
        print('Your plate is old')

    elif new_first.isdigit() and new_last.isupper():
        print('Your plate is new.')

    else:
        print('Your plate is invalid... Go check it at yur local police office.')

except:
    print('Your plate is invalid... Go check it at yur local police office.')
