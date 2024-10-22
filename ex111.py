numlist = []
input_text = ""

while input_text != "0":
    input_text = input("hi, type in a number")
    numlist.append(int(input_text))

numlist.sort(reverse=True)
print(numlist)
