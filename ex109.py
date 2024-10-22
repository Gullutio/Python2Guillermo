def magic_year(m, d, y):
    y = int(y[2] + y[3])
    if m * d == y:
        return "your date is truly magic"
    else:
        return "your date is not very magic"


month = int(input("type in a month in numbers"))
day = int(input("type in a day in numbers"))
year = str(input("type in your year in numbers"))
print(magic_year(month, day, year))
