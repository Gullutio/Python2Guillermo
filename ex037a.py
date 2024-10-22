print('HI')

try:
    value = int(input('HEllo please type in the value you want me to analyse: '))

    shapes = ['triangle', 'quadrilateral',
              'pentagon', 'hexagon', 'heptagon', 'octagon', 'nonagon']

    print(f'It is a {shapes[value - 3]}')

except ValueError:
    print('Sorry that is not a valid value. dont be sus !')
except IndexError:
    print('put a number between three and ten you sussybaka')
# subscriptable == joining strings concatinations. suscriptable == [ ]
# It is a heptagon            --------
#                            |  \(.) - (.)
 #                           | ________ \
#                            \___________|
