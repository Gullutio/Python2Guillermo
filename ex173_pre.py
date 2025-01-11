def factorial(n):
    final = 1
    if n != 0:
        for i in range(1, (int(n)+1)):
            final = final * i
    else:
        final = 1
    return final

input_text = input('type in positive number - ')
print(f'your factorial of {input_text} is {factorial(input_text)}')