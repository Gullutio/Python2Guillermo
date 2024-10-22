# Have to see if divisible by 400 if yes and is divisible by 4 and is not divisible by 100 is a leap year
# If else it is a leap year

# leap years : 2020 1996 1992 2004 2024 1904
# not a leap year: 2022 1900 2002 2001 1901 4000 1100

print('Helloo i am leap year bot')
print('I will calculate which years are leap years')


try:

    input_text = int(input('Type in your year ---> '))

    calc = input_text % 100

    if input_text % 400 == 0 and calc != 0 or input_text % 4 == 0 and calc != 0:
        print('Its a leap year')

    elif input_text <= 0:
        print('Brrrrr error!')

    else:
        print('Its not a leap year')

except:
    print('Brrrrr error!')
