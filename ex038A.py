# Ask the user for an input
# if its may 31 days if its february 28 to 29 days if its april 30 days etc

print(' HI I AM MONTH BOT')
month = input('Type in the month you want me to analyse ')
month = month.title()
d31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
d30 = ['April', 'June', 'Spetember', 'November']
dirr = 'February'


if month in d31:
    print('this month has 31 days')

elif month == dirr:
    print('This month has 28 to 29 days')

elif month in d30:
    print('This month has 30 days')

else:
    print('please write a month')
