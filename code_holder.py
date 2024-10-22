print('Hi')
x = int(input('Type first x value'))
y = int(input('Type first y value'))
x2 = input('Type in next x value')
if x2 != '':
    y2 = int(input('Type in next y value'))
    res = sqrt(((int(x) - int(x2))**2) + ((y - y2)**2))
    tot = res
else:
    print(res)
    quit


NEXT NEXT NEXT NEXT





    if (
                input[-1] == " "
                or input[-1] == "."
                or input[-1] == "!"
                or input[-1] == "?"
                or i[-1] == ","
                or i[-1] == ";"
                or i[-1] == ":"
            ):
                print(i)
                input.replace(input[-1], "")
                print(i)
            if (
                i[0] == " "
                or i[0] == "."
                or i[0] == "!"
                or i[0] == "?"
                or i[0] == ","
                or i[0] == ";"
                or i[0] == ":"
            ):
                print(i)
                i.replace(i[0], "")
                print(i)