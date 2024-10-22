# Ask the user for an input
# if its may 31 days if its february 28 to 29 days if its april 30 days etc

print(' HI I AM MONTH BOT')
month = input('Type in the month you want me to analyse ')
month = month.title()

if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    print('this month has 31 days')

elif month == 'February':
    print('This month has 28 to 29 days')

elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print('This month has 30 days')

else:
    print('please write a month')
