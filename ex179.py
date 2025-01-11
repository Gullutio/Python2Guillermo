#(old guess + new /guess) / 2
def square_root(n, guess=1.0):
    if abs(guess ** 2 - n) < 1e-12:
        return guess
    else:
        return square_root(n, (guess + n / guess) / 2)

if __name__ == "__main__":
    test_values = [4, 9, 16, 25, 2, 10]
    print("sqrt approximations:")
    for value in test_values:
        print(f"The sqrt of {value} is approximately {square_root(value)}")
