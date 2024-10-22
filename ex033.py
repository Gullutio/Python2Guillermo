print('You go into a bakery and want to buy bread.')
print('the day old bread sells for 60 percent less.')
bread = int(input('how many loaves of day old bread do you wanna buy? '))
F_BREAD = 3.49
D_BREAD = 3.49 * 60 / 100

calc1 = F_BREAD * bread
calc2 = D_BREAD * bread
calc3 = calc1 - calc2

print(f'{bread} loaves of fresh bread:   {calc1:.2f}$')
print(f'{bread} loaves of day old bread: {calc2:.2f}$')
print(f'You have saved {calc3:.2f}$ by buying day old bread')
