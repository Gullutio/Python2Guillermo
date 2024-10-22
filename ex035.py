# if the user enters a negative number we must tell him: NEXt time dont enter a negative number and the program stops
# if the user enter a number that is less than 2 we do take users input and multiply it by 10.5
# if the dog has 30 human years i type: you have broken the guinness world record for the longest living dog and continue the program
# we will always calculate  2 * 10.5 which is always 21 so we dont type it out
# minus 2 to human years and call the variable dy1  so we can then multiply that number by 4 to find how many dog years they are
# you then sum it up and see how many dog years the user's input makes
print('Wassup i will convert your human years to dog years')
hy = float(input('Hi type in how many human years you want me to convert: '))
if hy < 0:
    print('Sorry cant do try again after the program restarts')

elif hy < 2:
    dy1 = hy * 10.5
    print(f'Your dog is {dy1} years old')

elif hy > 49:
    print('try a less exagerated number next time')


else:
    dy1 = hy - 2
    dy2 = (dy1 * 4) + 21
    print(f'Your dog is {dy2} years old')
    if hy >= 30:
        print('You have broken the guinness world record for the longest living dog!')
