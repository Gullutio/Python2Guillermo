print('..............?!!?.....')

month = input('.what.month.where.u.born. --->').title()
try:
    day = int(input('.what.day.where.u.born. --->'))

    if (month == 'December' and day >= 22 and day <= 31) or \
            (month == 'January' and day >= 1 and day <= 19):
        print("Your astrological sign is capricorn")

    elif (month == 'January' and day >= 20 and day <= 31) or \
            (month == 'February' and day >= 1 and day <= 18):
        print("Your astrological sign is aquarius")

    elif (month == 'February' and day >= 19 and day <= 28) or \
            (month == 'March' and day >= 1 and day <= 20):
        print("Your astrological sign is pisces")

    elif (month == 'March' and day >= 21 and day <= 31) or \
            (month == 'April' and day >= 1 and day <= 19):
        print("Your astrological sign is aries")

    elif (month == 'April' and day >= 20 and day <= 30) or \
            (month == 'May' and day >= 1 and day <= 20):
        print("Your astrological sign is taurus")

    elif (month == 'May' and day >= 21 and day <= 31) or \
            (month == 'June' and day >= 1 and day <= 20):
        print("Your astrological sign is gemini")

    elif (month == 'June' and day >= 21 and day <= 30) or \
            (month == 'July' and day >= 1 and day <= 22):
        print("Your astrological sign is cancer")

    elif (month == 'July' and day >= 23 and day <= 31) or \
            (month == 'August' and day >= 1 and day <= 22):
        print("Your astrological sign is leo")

    elif (month == 'August' and day >= 23 and day <= 31) or \
            (month == 'September' and day >= 1 and day <= 22):
        print("Your astrological sign is virgo")

    elif (month == 'September' and day >= 23 and day <= 30) or \
            (month == 'October' and day >= 1 and day <= 22):
        print("Your astrological sign is libra")

    elif (month == 'October' and day >= 23 and day <= 31) or \
            (month == 'November' and day >= 1 and day <= 21):
        print("Your astrological sign is scorpio")

    elif (month == 'November' and day >= 22 and day <= 30) or \
            (month == 'December' and day >= 1 and day <= 21):
        print("Your astrological sign is sagittarius")

    else:
        print('Sorry that is not a valid value')

except:
    print('sorry thats not a valid value')
