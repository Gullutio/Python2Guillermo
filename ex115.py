def divisorer(input_text):
    divisors = []

    for i in range(input_text):
        if input_text % (i + 1) == 0:
            divisors.append(i + 1)
    divisors.pop(-1)
    return divisors


if __name__ == "__main__":
    input_text = int(input("type in a number"))
    print(divisorer(input_text))
