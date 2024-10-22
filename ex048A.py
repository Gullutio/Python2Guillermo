# CALC


print('Hello i am zodiac bot ')

input_text = int(input('please type in  the year u want me to analyse ---> '))
animals = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox',
           'Tiger', 'Hare', 'Dragon', 'Snake', 'Horse', 'Sheep']
calc = input_text % 12

print(f'your animal is {animals[calc]}')
