# start by:
# asking the user how many decibels he wants to write
# calculate if his decibelsk match any of the ones we have
# if not see if its in between any of them
# print the result

print('HI ;)!')
print('i am decibal bot and im deaf')
deci = int(input('write in how many decibels u want me to compare'))

if deci == 40:
    print('it is equal to a quiet room')

elif deci == 70:
    print('its equal to an alarm clock')

elif deci == 106:
    print('its equal to a gas lawnmower')

elif deci == 130:
    print('its equal to a jackhammer')

elif deci > 40 and deci < 70:
    print('your decibels are in between a quiet room and an alarm clock')

elif deci > 70 and deci < 106:
    print('your decibels are in between an alarm clock and a gas lawnmower')

elif deci > 106 and deci < 130:
    print(' your decibels are in between a gas lawnmower and a jackhammer')

else:
    print('write a value between 40 and 130')
