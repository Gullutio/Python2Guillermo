m = int(input('Enter the first value'))  # 38
n = int(input('Enter the second value'))  # 6
if m < n:
    d = m
else:
    d = n
while m % d != 0 or n % d != 0:
    d = d - 1
print(d)
