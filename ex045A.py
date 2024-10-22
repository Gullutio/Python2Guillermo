# Ask the user for a chess square
# check what letter the chess column is
# THen check if the square is an odd or even number
# if chess square is a, c, e, g + an odd number, the square = black
# if chess square is a, c, e, g + an even number, the square = white
# if chess square is b, d, f, h + an even number, the square = black
# if chess square is b, d, f, h + an odd number, the square = white


print('EHEllo im chess bot 2')
input_text = input('What chess square do you want me to analyse. ------>   ')

try:
    character = input_text[0]
    number = int(input_text[1:])

except:
    number = 10000000


letter_column = character

if number % 2 == 1:
    even_odd = 'odd'

else:
    even_odd = 'even'


if even_odd == 'odd' and (letter_column == 'a' or letter_column == 'c' or letter_column == 'e' or letter_column == 'g'):
    square = 'black'

elif even_odd == 'even' and (letter_column == 'a' or letter_column == 'c' or letter_column == 'e' or letter_column == 'g'):
    square = 'white'

elif even_odd == 'even' and (letter_column == 'b' or letter_column == 'd' or letter_column == 'f' or letter_column == 'h'):
    square = 'black'

elif even_odd == 'odd' and (letter_column == 'b' or letter_column == 'd' or letter_column == 'f' or letter_column == 'h'):
    square = 'white'

if number >= 9 or number <= 0:
    print('sorry that is not a valid value')

else:
    print(f'Your chess square is {square}')
