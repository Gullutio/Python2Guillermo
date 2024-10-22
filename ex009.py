INTEREST_1 = 10/100
INTEREST_2 = 10/100
INTEREST_3 = 10/100
print('Hello, i am GbankBot, i will tell you how much compound interest you will earn in 1,2 and 3 years.')
savings = float(input(
    'Enter how much money you want to put in your savings account. '))
calc_1 = savings * INTEREST_1 + savings
calc_2 = calc_1 * INTEREST_2 + calc_1
calc_3 = calc_2 * INTEREST_3 + calc_2

print(f'In 1 year you will get {calc_1:.2f}$.')
print(f'In 2 years you will get {calc_2:.2f}$')
print(f'In 3 years you will get {calc_3:.2f}$')
