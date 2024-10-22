import math

a = int(input("enter side 1 --- "))
b = int(input("enter side 2 --- "))


def hypotenuse(c, d):
    return math.sqrt(c**2 + d**2)


print(hypotenuse(a, b))
