months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
order = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def leapornot(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    day = int(input("type in a day - "))
    month = input("type in a month - ").title()
    year = int(input("type in a year - "))

    def ordinal_date(d, m):
        sum = 0
        for i in range(order[m] - 1):
            sum = sum + months[i + 1]
        sum = sum + d
        if leapornot(year):
            sum += 1
        return sum

    print(f"Your Ordinal Date is {ordinal_date(day, month)}")
