import random as r

update = 0
biggest = 0
for i in range(100):
    num = r.randint(1, 100)
    if num > biggest:
        biggest = num
        print(f"{num} --- Update")
        update += 1
    else:
        print(num)
print(f"{update} updates have been made including the first value.")
print(f"The highest value found was: {biggest}")