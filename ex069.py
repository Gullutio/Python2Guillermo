# Children less than or 2 years = no price
# 3 - 12 = 14$
# 65>= = 18$
# 12 - 65 = 23$
# cost needs to be displayed with 2 decimal points

print('hello')
price = 0

age = input('Type in an age')
while age != '':
    age = int(age)
    if 0 < age <= 2:
        price = price + 0

    elif 3 <= age <= 12:
        price = price + 14

    elif age >= 65:
        price = price + 18

    elif 12 < age < 65:
        price = price + 23

    age = input('Type in an age')

print(f'Your group price was {price:.2f}')
