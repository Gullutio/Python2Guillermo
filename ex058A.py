
# I want to get the value the user entered and then i take that and check in what list it is in.
# After thta i properly execute what I need to do with that value and print ou the appropiate date.
# If none of those dates are found or i get an error i will print invalid value.
# maybe i have to iterate thru that list until it matches th users month input

print('hi')
input_text = input(
    'Type in your date in this fashion --- year-month-day : 1998-5-24 --->  ')

try:
    date = input_text.split('-')  # list
    year = int(date[0])
    month = int(date[1])  # <--- Gets the month day and year and separates it.
    day = int(date[2])

    months_31 = [1, 3, 5, 7, 8, 10]
    # <---- is the list that keeps all the months that have 30 or 31 days.
    months_30 = [4, 6, 9, 11]

    # <----This checks if the input the user types in is at the end of the month.
    if (month in months_31 and day == 31) or (month in months_30 and day == 30) or (month == 2 and day == 28):
        month = month + 1
        day = 1
        print(f'Your date is ---> {year}-{month}-{day}')

    # <----- Checks if the day is not at the end of the month and does day + 1 and prints the next day.
    elif (month in months_30 and day >= 1 and day <= 29) or (month in months_31 and day >= 1 and day <= 30) or (month == 2 and day >= 1 and day <= 28):
        day = day + 1
        print(f'Your date is ---> {year}-{month}-{day}')

    elif month == 12 and day == 31:
        month = 1
        day = 1
        # <---- Checks if it is the last day of the year and I change year.
        year = year + 1
        print(
            f'Your date is ---> {year}-{month}-{day}, Happy new year user I have never met in my life and I will probably never see...!')
    else:
        # <----- If none of these happen it is an invalid value
        print('i̴̢̯̱̰̘͇͉̥͊͋͂̓̔͂̕ṇ̵̢̡̨̪̩͙̝̀͐̒̾̓͛v̶̢̢͖̤̱̺̼̯͔́̉̒̓͆̇͐͒̃̓̍̈́̾̾̚ā̶̡̲̭̙̭͎̹̖͚̺̼̗̞͊̔͊̈́̑́̿̍̎͐̀ͅl̸̢̨̙͍̗̦̪͍͎̪͐̀͑̐̏̾͋͘͜͝i̴̛̭̖̼͎̐̐̓̄̌͝ḑ̴̯̱̩̞̠͔͕͍̥̺̤͑̾̈̓̕ ̸̹͂̑͛̿͊̄̋̂̃̅̌̉̾v̸̢̢͙͙̤̠̝̬͚̳̤̝̟̂̃a̵̡̛̰͖̟̠̭̪̱̖͙̗̪̞͚̯̿̉̾͋̎́̄̈̓̆͂̑͝l̵̗̬͙̥̼̭̐͊̂̒u̶̡͚̼̖͍̫̟̙̹̯̓̀̋͋͊̔͠ͅé̴̢̬̯̖͕̲̍͆͐̓͝')
except:
    # <---- If there is an error tell the user by prininting out invalid value.
    print('i̴̢̯̱̰̘͇͉̥͊͋͂̓̔͂̕ṇ̵̢̡̨̪̩͙̝̀͐̒̾̓͛v̶̢̢͖̤̱̺̼̯͔́̉̒̓͆̇͐͒̃̓̍̈́̾̾̚ā̶̡̲̭̙̭͎̹̖͚̺̼̗̞͊̔͊̈́̑́̿̍̎͐̀ͅl̸̢̨̙͍̗̦̪͍͎̪͐̀͑̐̏̾͋͘͜͝i̴̛̭̖̼͎̐̐̓̄̌͝ḑ̴̯̱̩̞̠͔͕͍̥̺̤͑̾̈̓̕ ̸̹͂̑͛̿͊̄̋̂̃̅̌̉̾v̸̢̢͙͙̤̠̝̬͚̳̤̝̟̂̃a̵̡̛̰͖̟̠̭̪̱̖͙̗̪̞͚̯̿̉̾͋̎́̄̈̓̆͂̑͝l̵̗̬͙̥̼̭̐͊̂̒u̶̡͚̼̖͍̫̟̙̹̯̓̀̋͋͊̔͠ͅé̴̢̬̯̖͕̲̍͆͐̓͝')


# ______________________LEARNING POINTS_________________________________________
# I learned how to minimize several if statements with similarities into one
# I learned how to split a value into several pieces
