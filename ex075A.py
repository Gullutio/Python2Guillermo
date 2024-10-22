# get an user input
# Compare the first letter of the user input with the last letter of the user input.
# FRom the first letter shift 1 letter to the right
# From the last letter, shift one letter to the left
# Compare them and continue the process until you reach the middle or you find a pair that doesnt/ match.
is_palindrome = True
input_text = input('type - ').lower()
for i in range(len(input_text) // 2):
    # right = len(input_text) - i - 1 gets index from left to right
    right = - i - 1  # gets index from right to left.
    if input_text[i] != input_text[right]:
        print('this aint a palindrome')
        is_palindrome = False
        break
if is_palindrome:
    print('this is a palindrome.')
