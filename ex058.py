# ask the user for what date they want to calculate
# take away the -
# Check  if it's the last day of that month and if yes set month to month+1 and day to 1 with my dictionary
# if not do day = day + 1
# print the final value

print('hi')
input_text = input(
    'Type in your date in this fashion --- year-month-day : 1998-5-24 --->  ')

try:
    date = input_text.split('-')  # list
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and day == 31:
        month = month + 1
        day = 1
        print(f'Your date is ---> {year}-{month}-{day} .')

    elif (month == 4 or month == 6 or month == 9 or month == 11) and day == 30:
        month = month + 1
        day = 1
        print(f'Your date is ---> {year}-{month}-{day}')

    elif month == 2 and day == 28:
        month = month + 1
        day = 1
        print(f'Your date is ---> {year}-{month}-{day}')

    elif (month == 4 or month == 6 or month == 9 or month == 11) and day >= 1 and day <= 29:
        day = day + 1
        print(f'Your date is ---> {year}-{month}-{day}')

    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and day >= 1 and day <= 30:
        day = day + 1
        print(f'Your date is ---> {year}-{month}-{day}')

    elif month == 2 and day >= 1 and day <= 28:
        day = day + 1
        print(f'Your date is ---> {year}-{month}-{day}')

    elif month == 12 and day == 31:
        month = 1
        day = 1
        year = year + 1
        print(
            f'Your date is ---> {year}-{month}-{day}, Happy new year user I have never met in my life and I will probably never see...!!!')

    else:
        print('invalid value')

except:
    print('invalid value')
