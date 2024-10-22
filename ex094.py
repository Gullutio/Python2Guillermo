len1 = int(input("Type in first length"))
len2 = int(input("Type in second length"))
len3 = int(input("Type in third length"))


def valid_invalid(l1, l2, l3):
    if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
        return False
    else:
        return True


print(valid_invalid(len1, len2, len3))
