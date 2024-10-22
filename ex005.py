SMALL_DEPOSIT = 0.10
BIG_DEPOSIT = 0.25

print('Heyo im recycleBot, enter the ammount of big bottles and small botlles you want to recycle.')
small_bottles = input(
    'Enter the number of small botlles you want to recycle. ')
big_bottles = input('Enter the nuber of big bottles you want to recycle. ')
calculate_small = float(small_bottles) * SMALL_DEPOSIT
calculate_big = float(big_bottles) * BIG_DEPOSIT
total = float(calculate_small) + float(calculate_big)
print(f'You got {total}$.')
