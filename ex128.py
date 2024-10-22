def count_range(e_list, max, min):

    total = 0
    for i in e_list:
        if i >= min and i <= max:
            total += 1
    return total

ele_list = []

while True: 
    input_text = input('Please add in some numbers here and type and empty space when youre done! --- ')
    if input_text == "":
        break
    ele_list.append(float(input_text))

min_val = float(input('type in your min value --- '))
max_val = float(input('type in your max value --- '))

print(f'You have {count_range(ele_list, max_val, min_val)} numbers in between your minimum and maximum values.') 