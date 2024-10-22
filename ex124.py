x = 0
y = 0
m = 0
n = 0
sigx = 0
sigy = 0
sigxy = 0
pwr = 0

while True:
    x = input("type in your x variable")
    if x == "":
        break
    y = input("type in your y variable")

    if x != "" and y != "":
        n += 1
        x = float(x)
        y = float(y)
        sigxy += x*y
        sigx += x
        pwr += float(x ** 2)
        sigy += y
    else:
        break #1.9 , 24

m = (sigxy - (sigx * sigy)/n) / (pwr - ((sigx ** 2)/n))
b = sigy/n - (m *(sigx/n))
print (f'Your Line of Best Fit is: y = {m:.2f}x + {b:.2f}')
