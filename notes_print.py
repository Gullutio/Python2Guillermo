day = 24
month = "May"
year = 2011
price = 12.34567

# The date is 24 May 2011.
print("The date is " + str(day) + " " + month + " " + str(year) + ".")
print("The date is", day, month, str(year) + ".")
print("The price of a beanbag is", str(price) + "SG$.")
print(f"The price of a beanbag is {price:.2f}SG$.")


food = ["Pineapple", "Burger", "Pizza"]
prices = [10, 2.99, 7.4]

# MENU
# -------------------------------
# Pineapple...............$ 10.00
# Burger..................$  2.99
# Pizza...................$  7.40

print("MENU")
print("-" * 30)
print(f"{food[0]:.<24s}$ {prices[0]:5.2f}")
print(f"{food[1]:.<24s}$ {prices[1]:5.2f}")
print(f"{food[2]:.<24s}$ {prices[2]:5.2f}")
food[0]


print("Guillermo", end="\n")
print("Camba")
