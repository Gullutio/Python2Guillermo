ANCH = 2.54
FAAT = 12 * ANCH

print('halo i am metric system whatnot converting machine...')
feet = float(input('Enter the number of feet you wanna convert to cm. '))
inch = float(input('Enter the number of inches you wanna convert to cm. '))
conv_inch = inch * ANCH
conv_feet = feet * FAAT
total = conv_inch + conv_feet
print(f'{feet} feet and {inch} inches = {total}cm.')
