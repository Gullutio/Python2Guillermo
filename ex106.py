def month_calc(month, year):
    months_31 = [1, 3, 5, 7, 8, 10]
    months_30 = [4, 6, 9, 11]

    if month in months_30:
        return 30
    elif month in months_31:
        return 31
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 29
    else:
        return 28


if __name__ == "__main__":
    months = int(input("type in a month number"))
    years = int(input("type in a year"))
    print(month_calc(months, years))
