from math import sqrt

# User keys in 1st point
# User keys in 2nd point do the formula
# user continues putting more points
# User ends the program
# add up all the values and ur done
print('hi, i am near ex100. ME HAPPY! and sad at same time. Please type in an empty string in the x when you want to finalise your values')


x2 = input(
    'Please type in a number to continue the program. Type in a blank line to stop it.')


while x2 != '' or x != '':
    # point =
    x = input('Type in x coordinate number 1')
    y = int(input('Type in y coordinate number 1'))
    x2 = input('Type in x coordinate number 2')
    y2 = int(input('Type in y coordinate number 2'))
    res = int(sqrt(((x - x2)**2) + ((y - y2)**2)))

print(res)
