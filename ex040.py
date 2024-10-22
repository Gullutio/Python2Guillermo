# ask the user for values
# do comparison of the 3 values to see which one it is
# print the type of triangle it is
# check if s1 is equal to s2 and then check if s3 is different to s1/ check if s1 is equal to s3 and then check if s2 is different from s1
# sum s1 , s2 and s3 then check for max and minus it to the sum if max is bigger than the sum

print('hi i am triangle bot')
s1 = float(input('please write the length in cm of your first side '))
s2 = float(input('please write the length in cm of your second side '))
s3 = float(input('please write the length in cm of your second side '))
calc = (s1 + s2 + s3) - max(s1, s2, s3)
#(s1 + s2) <= s3 or (s1 + s3) <= s2 or (s2 + s3) <= s1

if max(s1, s2, s3) > calc or s1 < 1 or s2 < 1 or s3 < 1:
    print('PLEASE ENTER A MORE REASONABLE VALUE')

elif s1 == s2 == s3:
    print('It is an equalateral')

elif s1 == s2 or s1 == s3 or s2 == s3:
    print('your triangle is isoceles')

elif s1 != s2 != s3:
    print('this triangle is scalene')
