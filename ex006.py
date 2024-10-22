TIP_PERCENTAGE = 18/100
TAX_PERCENTAGE = 6/100

food_worth = float(input('Enter how many dollars worth of food you want. '))
tip = food_worth * TIP_PERCENTAGE
tax = food_worth * TAX_PERCENTAGE
total = tip + tax + food_worth
print('-'*40)
print(f'{"cost of food":20s} :${food_worth:13.2f}')
print(f'{"tip":20s} :${tip:13.2f}')
print(f'{"tax":20s} :${tax:13.2f}')
print('='*40)
print(f'{"total"} :${tax + tip + food_worth:13.2f}')
