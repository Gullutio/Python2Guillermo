averager = 0
above = []
below = []
numbers = []
input_text = 0

while True:
    input_text = input("type in a number")
    if input_text == "":
        break
    numbers.append(int(input_text))
    averager += int(input_text)
averager /= len(numbers)

for x in range(len(numbers)):
    if numbers[x] > averager:
        above.append(str(numbers[x]))
    if numbers[x] < averager:
        below.append(str(numbers[x]))
    if numbers[x] == averager:
        input_text = averager

print(
    f"your above average numbers are {','.join(above)} your below average are {','.join(below)} and your average numbers(if any) are {input_text}"
)
