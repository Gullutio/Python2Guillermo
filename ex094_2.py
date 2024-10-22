len1 = int(input("Type in first length"))
len2 = int(input("Type in second length"))
len3 = int(input("Type in third length"))


def valid_invalid(l1, l2, l3):
    if (l2 + l3) - l1 <= 0 or (l1 + l3) - l2 <= 0 or (l2 + l1) - l3 <= 0:
        return False
    else:
        return True