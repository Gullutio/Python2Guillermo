num1 = input("type in your first number")
num2 = input("type in your second number")
num3 = input("type in your third number")


def calc(a, b, c):
    big = int(max(a, b, c))
    small = int(min(a, b, c))
    median = (int(a) + int(b) + int(c)) - ((big) + (small))
    return f"your median is {median}"


print(calc(num1, num2, num3))
