factor = 2
n = int(input('type in number thats more than 2 --- '))
print(f'The prime factors of {n} are:')
while factor <= n:
    if n % factor == 0:
        n = n//factor
        print(factor)
    else:
        factor += 1
