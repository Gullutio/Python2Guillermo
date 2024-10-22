def sorter(input_text):
    ascending = []
    descending = []
    ascending += input_text
    descending += input_text
    ascending.sort()
    descending.sort(reverse = True)
    return ascending == input_text or descending == input_text

input_text = "initial val"
list_n = []

while True: 
    input_text = input('Please add in some numbers here and type and empty space when youre done! --- ')
    if input_text == "":
        break
    list_n.append(int(input_text))

print(sorter(list_n))