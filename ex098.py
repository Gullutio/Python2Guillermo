def prime_or_not(integer):
    for i in range(1, integer + 1):
        if integer % i == 0:
            integer += i
    if integer == 12:
        return True
    else:
        return False


if __name__ == "__main__":
    integer = int(input("write in a value"))
    print(prime_or_not(integer))
