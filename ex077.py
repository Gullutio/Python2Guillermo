# Start by making a variable with numbers 1 to 10(variable A)
# Make another vaiable that starts with 1 and goes up to 10(variable B)
# We will first start by printing a line with the numbers 1 to 10.
# then we will go to the next line and print var B
# increase var B by 1 and multiply it by var A and print the result in the same line.
# When done with line reset b and add 1 to A
# Redo the same thing 10 times
print('      1    2    3    4    5    6    7    8    9   10')
for a in range(1, 11):
    res = ''
    for b in range(1, 11):
        calc = (f'{b * a:5.0f}')
        res = (res + str(calc))
    print(str(f'{a:2.0f}') + res)
