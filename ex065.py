print('Im tired of converting but here we go')

# celsius to farenheit
# .conversion table
# 10, 20, 30, 40, 50, 60, 70, 80, 90 and 100. all multiples of 10 until 100
#celsius * 1.8 +32
in_val = 0  # <----sets initial value
for i in range(11):  # has to repeat 11 times to print all the values
    print(f'{in_val}°C = {in_val * 1.8 + 32:.0f}°F')  # prints the conversion
    # <---Adds 10 because i have to use all the multiples of 10 from 0 100
    in_val = in_val + 10
