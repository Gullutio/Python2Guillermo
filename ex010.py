print('Hello, I will sum, substract and show the product of the numbers you type in.')
a = float(input('Place your first number here.'))
b = int(input('Place your second number here.'))
add = a + b
sub = b - a
mul = a * b
div = a % b
pwr = a ** b
quo = a // b

print(f'{a} + {b} = {add}')
print(f'{a} - {b} = {sub}')
print(f'{a} × {b} = {mul}')
print(f'{a} // {b} = {quo}')
print(f'{a} |x| {b} = {div}')
print(f'{a} ** {b} = {pwr}')
