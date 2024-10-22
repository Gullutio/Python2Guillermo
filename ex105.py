hexnums = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15",
}


def base_to_int(_input, base):
    i2 = 0
    dec = 0
    for i in _input:
        i2 += 1
        dec += int(hexnums[i]) * (int(base) ** (len(_input) - i2))
    return dec


def int_to_base(_input, base):
    base = int(base)
    remain = ""
    rev_hexnums = dict()
    dec = _input
    for key in hexnums:
        val = hexnums[key]
        rev_hexnums[val] = key
    while dec != 0:
        remain = rev_hexnums[str(int(dec) % int(base))] + remain  # problem here
        dec = int(dec) // int(base)

    return remain


input_base = input("type in a base number to convert to base 10 - ")
input_text = input("type in a integer number to convert - ")
print(base_to_int(input_text, input_base))

input_base = input("type in a base number to convert to from base 10 - ")
input_text = input("type in a integer number to convert - ")
print(int_to_base(input_text, input_base))
