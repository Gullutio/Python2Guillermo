print('hi')
input_text = input(
    'Please type in a canada national holiday month and day example: December 25 ').title()

holiday = {'December 25': 'Christmas Day',
           'July 1': 'Canada Day', 'January 1': "New Year\'s Eve"}

try:
    print(f'Your holiday is {holiday[input_text]}')

except:
    print('Sorry that is not a valid holiday')
