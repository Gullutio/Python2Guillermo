print('Hello i am second calculator nummber 2')

print('I will calculate how many seconds you wanna calculate into days hours minutes and seconds.')
seconds_original = int(input(
    'Please type in the amount of seconds you wanna turn into days hours minutes and seconds '))

seconds = seconds_original
conv_days = seconds // 86400
seconds = seconds % 86400
conv_hours = seconds // 3600
seconds = seconds % 3600
conv_minutes = seconds // 60
seconds = seconds % 60
conv_seconds = seconds // 1
seconds = seconds % 1

print(f'{seconds_original:0>2d} seconds are calculated into {conv_days:0>2d} days, {conv_hours:0>2d} hours, {conv_minutes:2d} minutes and {conv_seconds:2d} seconds.')

print(f'{conv_days:0>2d}:{conv_hours:0>2d}:{conv_minutes :0>2d}:{conv_seconds :0>2d}')
