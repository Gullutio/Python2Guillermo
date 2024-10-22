print('Hi i am us banknote reading bot')
input_text = int(
    input('pls type in the ammount of money u want me to analyse: '))
banknotes = {1: 'George Washington', 2: 'Thomas Jefferson', 5: 'Abraham Lincoln',
             10: 'Alexander Hamilton', 20: 'Andrew Jackson', 50: 'Ulysses S. Grant', 100: 'Benjamin Franklin'}

print(f'The individual on your banknote is {banknotes[input_text]}')
