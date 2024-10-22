# Spring = March 20 - June 20
# Summer = June 21 - September 21
# Fall = September 22 - December 20
# Winter = December 21 - March 19
# December 1 = Fall
# November 2 = Fall
# October 16 = Fall
# September 20 = Fall
# January 7 = Winter
# February 20 = winter
# December 25 = Winter
# MArch 10 10 = Winter
# June 30 = Summer
# September 20 = SUmmer
# july 4 = Summer
# Agust 10 = Summer
# May 24 = Spring
# March 20 = spring
# June 19 = spring
# April 1 = spring

# Create 4 lists with each ahving  all the months and days in their season
# Check if the users imput matxches the month and day in anny of the 4 lists
# if it doesnt or there are any errors print sorry that is not a valid input

print('Hi i am season bot.')
month = input('Please type in the month u want me to analyse ---> ').title()
try:
    day = int(input('Please type in the day u want me to analayse ---> '))

    if (month == 'March' and day >= 21 and day <= 30) or \
        (month == 'June' and day >= 1 and day <= 20) or \
        (month == 'April' and day >= 1 and day <= 30) or \
            (month == 'May' and day >= 1 and day <= 31):
        print("Hey, this month's season is spring!")

    elif (month == 'June' and day >= 20 and day <= 31) or \
        (month == 'September' and day >= 1 and day <= 21) or \
        (month == 'July' and day >= 1 and day <= 31) or \
            (month == 'August' and day >= 1 and day <= 31):
        print("Hey, this month's season is summer!")

    elif (month == 'September' and day >= 22 and day <= 30) or \
        (month == 'December' and day >= 1 and day <= 20) or \
        (month == 'October' and day >= 1 and day <= 31) or \
            (month == 'November' and day >= 1 and day <= 30):
        print("Hey, this month's season is fall!")

    elif (month == 'December' and day >= 21 and day <= 31) or \
        (month == 'March' and day >= 1 and day <= 19) or \
        (month == 'January' and day >= 1 and day <= 31) or \
            (month == 'February' and day >= 1 and day <= 29):
        print("Hey, this month's season is winter!")

    else:
        print('sorry thats not a valid value')

except:
    print('Sorry thats not a valid value')
