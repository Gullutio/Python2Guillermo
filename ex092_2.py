import ex091

order = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

date = int(input("Type in an ordinal date - "))
year = int(input("Type in a year - "))
sum = 0
iter = 0
place = date


def calc(d, s, i, p, y):
    while d > s:
        print(i)
        i += 1
        s = s + ex091.months[i]
    d = s - d
    d = ex091.months[i] - d
    print(d)
    return f"The ordinal date, {p} translates to {order[i]} {d} {y}"


print(calc(date, sum, iter, place, year))
