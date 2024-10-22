# user types in input
#abs(g*g - x)
x = int(input('Hi type in a number --- '))
guess = x/2
while abs(guess * guess - x) > 10**-12:
    guess = (guess + x/guess) / 2
print(f'The square root of {x} is {guess}')
# if abs(guess * guess - x) <= 10**-12:
