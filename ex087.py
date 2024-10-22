items = int(input("How many items are you buying today?"))


def fee(i):
    items = i - 1
    cost = (items * 2.95) + 10.95
    return f"the price of shipping for {i} items is: {cost:.2f}$"


print(fee(items))
