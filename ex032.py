print('Hi you will write 3 numbers')

int1 = int(input('write 1st number'))
int2 = int(input('2nd number'))
int3 = int(input('3rd number'))

big = max(int1, int2, int3)
small = min(int1, int2, int3)

compute = int1 + int2 + int3 - big - small

print(
    f'The biggest number is {big}, the middle number is {compute} and the smallest number is {small}.')
