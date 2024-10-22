import random as r

plate = ""


def plate_chooser(plate):
    old_new = r.randint(0, 1)
    if old_new == 1:
        for i in range(3):
            plate += chr(r.randint(65, 122))
        for i in range(3):
            plate += chr(r.randint(48, 57))
    else:
        for i in range(4):
            plate += chr(r.randint(48, 57))

        for i in range(3):
            plate += chr(r.randint(65, 122))
    return plate


print(plate_chooser(plate))
