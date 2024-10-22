def outlier():
    for i in range(1):
        numlist.pop(0)
        numlist.pop(len(numlist) - 1)
    return numlist


numlist = []
input_text = input("hi, type in a number")

while input_text != "0":
    numlist.append(input_text)
    input_text = input("hi, type in a number")

if len(numlist) >= 4:
    numlist.sort()
    print(f"{numlist} --- original")
    print(f"{outlier()} --- modified ")

else:
    print("error")
