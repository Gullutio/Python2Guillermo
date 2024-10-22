a_string = input('Hi!')
left = 0
right = len(a_string) - 1

while left < right:
    # compare
    # if chars are not the same, break
    if a_string[left] != a_string[right]:
        print('this is not a palindrome')
        break
    # if chars are the same, increase left, decrease right
    else:
        left += 1
        right -= 1
# anna  sus
if left >= right:
    print('This is a palindrome')
 