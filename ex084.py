import random as r

finalflips = 0
for i in range(10):
    counter = 0
    last = 0
    flips = 0
    flipper = 0
    while counter != 3:
        last = flipper
        flipper = r.randint(0, 1)
        flips += 1
        if flipper == 1 and last == 1:
            print("H", end=" ")
            counter = counter + 1
        elif flipper == 0 and last == 0:
            print("T", end=" ")
            counter = counter + 1
        elif flipper == 0 and last == 1:
            print("T", end=" ")
            counter = 1
        elif flipper == 1 and last == 0:
            print("H", end=" ")
            counter = 1
    print(f"{flips} flips")
    finalflips += flips
print(f"{finalflips} total flips")
print(f"{finalflips/ 10} average")
