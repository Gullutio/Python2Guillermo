from random import choice

final = 0
for _ in range(10):
    prev = ""
    flips = 0
    count = 0  # count tails
    while count < 3:
        # flip a coin
        face = choice(["H", "T"])
        # print the coin
        print(face, end=" ")
        # adjust count
        if face == prev:
            count += 1
        elif face != prev:
            count = 1
        prev = face
        flips += 1
    print(f"({flips} flips)")
    final += flips
print(f"{final} total flips")
print(f"{final / 10} average flips")


# H T H T H H T T T
