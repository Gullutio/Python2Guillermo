from math import sqrt

# User keys in 1st point
# User keys in 2nd point do the formula
# user continues putting more points
# User ends the program
# add up all the values and ur done
print('hi, i am near ex100. ME HAPPY! and sad at same time. Please type in an empty string in the x when you want to finalise your values')

final = 0

while x2 != '' or x != '':
    # point =
    x = input('Type in x coordinate number 1 ---> ')
    if x == '':
        res = sqrt(((int(x) - int(x2))**2) + ((y - y2)**2))
        final = final + res
        break
    else:
        y = int(input('Type in y coordinate number 1 ---> '))
        x2 = input('Type in x coordinate number 2 ---> ')
        if x2 == '':
            res = sqrt(((int(x) - int(x2))**2) + ((y - y2)**2))
            final = final + res
            break
        else:
            y2 = int(input('Type in y coordinate number 2 ---> '))
            res = sqrt(((int(x) - int(x2))**2) + ((y - y2)**2))
            final = final + res

print(final)
