import random

randnums = []
for i in range(6):
    numcheck = 0
    while numcheck in randnums or numcheck == 0:
        numcheck = random.randint(1, 49)
    randnums.append(numcheck)
randnums.sort()
print(randnums)
