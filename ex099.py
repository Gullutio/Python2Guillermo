import ex098

input_text = int(
    input("hello type in a number and i will tell you its next prime number")
)


def nextprime(input):
    if ex098.prime_or_not(input):
        input += 1
        while ex098.prime_or_not(input) == False:
            input += 1
    else:
        while ex098.prime_or_not(input) == False:
            input += 1

    return f"Your closest prime number is {input}"


print(nextprime(input_text))
