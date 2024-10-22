term = int(input('Enter a number --- '))
while term != 1:
    print(term)
    if term % 2 == 0:
        term = term // 2
    else:
        term = term*3+1

print(term)
