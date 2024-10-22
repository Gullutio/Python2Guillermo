
print('Please enter a date in this format --- Year-Month-Day --- example --- 2012-1-7')
input_text = input('Pls type in a value')

date = input_text.split('-')  # list
year = int(date[0])  # string
month = int(date[1])  # string
day = int(date[2])  # string

# THe bug is somewhere over here...


# try:
# string and string for the test case 2011-5-24 goes in here and comes out as 2011-6-1 because of the or month ==

if day != 31:
    day = day + 1
    print(f'Your date is ---> {year}-{month}-{day}')
    # ok so now i have to do some test cases to see if everything works YAYAY!!!!!

elif day != 29:
    day = day + 1
    print(f'Your date is ---> {year}-{month}-{day}')
    # ok so now i have to do some test cases to see if everything works YAYAY!!!!!

elif day != 30:
    day = day + 1
    print(f'Your date is ---> {year}-{month}-{day}')
    # ok so now i have to do some test cases to see if everything works YAYAY!!!!!


elif day == 31 and month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 or month <= 12:
    print('jsjsjsjjsjsjs')
    month = month + 1
    day = 1
    print(f'Your date is ---> {year}-{month}-{day}')

elif day == 30 or month == 4 or month == 6 or month == 9 or month == 11 and month <= 12:  # string and string
    month = month + 1
    day = 1
    print(f'Your date is ---> {year}-{month}-{day}')

elif day == 31 or month == 12 and month <= 12:  # string and string
    month = month + 1
    day = 1
    print(f'Your date is ---> {year}-{month}-{day}')

elif month == 12 and day == 24:
    month = 1
    day = 1
    year = year + 1
    print(f'Your date is ---> {year}-{month}-{day}')

elif month == 2 and day == 29:
    month = month + 1
    day = 1
    print(f'Your date is ---> {year}-{month}-{day}')

else:
    print('invalid value')

# except:
#    print('invalid value')


# elif month == 1 and day == 31:
    # month = 2
    # day = 1

# ['100', '200', '300']
# sussy == '100'
