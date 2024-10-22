print('Hello, I am self changing checkout...um...whatever machine.')
dollars = float(input('Enter how much change you want in dollars. '))
# its multiplying the value from line 2 by 100 and setting it to cents
cents = dollars * 100
conv_too = cents // 200  # Its dividing cents by 200 and taking out the decimal numbers and setting it to conv_too. conv too contains the number of toonies we need
# Its getting the remainder of cents divided by 200 and then gets the remainder set the value to cents
cents = cents % 200
conv_loo = cents // 100  # 1 loonie = 100 cents
cents = cents % 100
conv_qua = cents // 25
cents = cents % 25
conv_dim = cents // 10
cents = cents % 10
conv_nic = cents // 5
cents = cents % 5
conv_pen = cents // 1
cents = cents % 1

print(f'toonies  = {conv_too}')
print(f'loonies  = {conv_loo}')
print(f'quarters = {conv_qua}')
print(f'dimes    = {conv_dim}')
print(f'nickles  = {conv_nic}')
print(f'pennies  = {conv_pen}')
