from math import remainder


print(':[ sad')

input_text = 0
penn = 0

while input_text != '':

    penn = int(input_text) + penn
    input_text = input('Type: ')

print(penn)
# print(nums * 100)
remainder = penn % 5

if remainder > 2.5:
    nicks = (penn - remainder + 5)
    print(nicks)


elif remainder < 2.5:
    remainder = (penn - remainder)
    print(remainder)
 