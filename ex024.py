print('Hello, I am second calculator, Please enter the values for how many days, hours minutes and seconds you want to turn to second.')
days = int(input('How many days u wanna turn to seconds '))
hours = int(input('How many hours u wanna turn to seconds '))
mins = int(input('How many mins u wanna turn to seconds '))
secs = int(input('How many secs u wanna turn to seconds '))
calc = days * 86400 + hours * 3600 + mins * 60 + secs
print(f'Your final calculation is {calc} seconds.')
