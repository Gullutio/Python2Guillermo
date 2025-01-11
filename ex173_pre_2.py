def factorial(n):
    final = 1
    while n != 0:
        final = final * n
        n = n -1
        factorial(n)
    return final


# input_text = input('type in positive number - ')
# print(factorial(int(input_text)))



def factorial1(n):
    # Base case: 0 and 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: 
    return n * factorial(n-1)

print(factorial(int(input('n: '))))