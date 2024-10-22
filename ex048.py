# 1 - get an input from the user and make a dictionary with all the years and the animals that correspond to them
# then divide the number they gave you by twelve and search for the index equivalent to the rest in your dictionary
# then print it out saying that that is their animal
# 2 - get an input from the user then divide it by 12 and use the remainder to get a bunch of if statements that tell you what animal your year is

print('hi')
try:
    input_text = int(input(
        'Hi what zodiac animal do you wanna choose, please write in a number!?'))

    calc = input_text % 12

    if input_text <= -1:
        print('Sorry that is not a possible number')

    elif calc == 8:
        zodiac = 'Dragon'

    elif calc == 9:
        zodiac = 'Snake'

    elif calc == 10:
        zodiac = 'Horse'

    elif calc == 11:
        zodiac = 'Sheep'

    elif calc == 0:
        zodiac = 'Monkey'

    elif calc == 1:
        zodiac = 'Rooster'

    elif calc == 2:
        zodiac = 'Dog'

    elif calc == 3:
        zodiac = 'Pig'

    elif calc == 4:
        zodiac = 'Rat'

    elif calc == 5:
        zodiac = 'Ox'

    elif calc == 6:
        zodiac = 'Tiger'

    elif calc == 7:
        zodiac = 'Hare'

    print(f'Your animal is a {zodiac}')
except:
    print('not a valid value')
