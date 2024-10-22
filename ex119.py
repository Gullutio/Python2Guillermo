averager = 0
above = []
below = []
numbers = []
input_text = 0

while True:
    input_text = input("type in a number")
    if input_text == "":
        break
    numbers.append(input_text)
    averager += int(input_text)
averager /= len(numbers)

for number in numbers:
    if int(number) > averager:
        above.append(number)
    if int(number) < averager:
        below.append(number)
    if int(number) == averager:
        input_text = averager
print(
    f"your above average numbers are {','.join(above)} your below average are {','.join(below)} and your average numbers(if any) are {input_text}"
)
