def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

if __name__ == "__main__":
    try:
        n = int(input('enter a number - '))
        if n < 0:
            print("Please enter a non-negative number.")
        else:
            print(f"The binary for {n} is: {decimal_to_binary(n)}")
    except ValueError:
        print("oops, invalid!")
