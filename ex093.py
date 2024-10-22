def centerer(s, w):
    if len(s) >= w:
        return s

    elif len(s) < w:
        return " " * ((int(w) - len(s)) // 2) + s


string = input("enter in a string")
width = int(input("enter in a number"))
print(centerer("li", width))
print(centerer("boing", width))
print(centerer(string, width))
