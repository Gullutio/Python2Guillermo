import ex091


def convert(d, y):
    sum = 0
    month = 0
    or_date = d
    """
    Converts Ordinal to Gregorian dates.
    param d = day
    param s = sums up all the days that the months have

    """
    # <----- Converts Ordinal to Gregorian dates.
    # d = day
    # s = sums up all the days that the months have
    # i = iterates throught the months
    # p = placeholder for the initial input
    # y = year
    if ex091.leapornot(year):
        ex091.months[2] = 29  # <----- function
    while d > sum:
        month += 1
        sum = sum + ex091.months[month]
    d = sum - d
    d = ex091.months[month] - d
    return f"The ordinal date, {or_date} translates to {compare[month]} {d} {y}"


compare = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",  # <------ main program starts here
    10: "October",
    11: "November",
    12: "December",
}
day = int(input("Type in an ordinal date - "))
year = int(input("Type in a year - "))


print(convert(day, year))
