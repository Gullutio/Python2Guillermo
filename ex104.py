import random as r

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


def hex2int():
    return f"hex value - {input_text} is equal to the decimal value of {hexnums[input_text.capitalize()]}"


def int2hex():
    rev_hexnums = dict()
    for key in hexnums:
        val = hexnums[key]
        rev_hexnums[val] = key
    return f"decimal value - {input_text} is equal to the hex value of {rev_hexnums[input_text.capitalize()]}"


if __name__ == "__main__":
    try:
        input_text = input("Type in a hexanumerical character from 1 to F --- ")
        print(hex2int())
        input_text = input("Type in a decimal value from 1 to 15 --- ")
        print(int2hex())
    except:
        print("your value is invalid try again later")
