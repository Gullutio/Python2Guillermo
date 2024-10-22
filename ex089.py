def convert(p):
    ordinal = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelvth",
    }
    return ordinal[p + 1]


if __name__ == "__main__":
    for i in range(12):
        print(convert(i))
