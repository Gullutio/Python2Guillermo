print("Hello")
sum = 0
lastr = 0
input_text = input("type in a binary number(100110)")
mult = len(input_text) - 1
for i in input_text:
    calc = int(i) * (2**mult)
    sum = sum + calc
    mult = mult - 1
print(f"binary number, {input_text} in decimal form is: {sum}")
