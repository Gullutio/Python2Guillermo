def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

if __name__ == "__main__":
    a, b = map(int, input("enter two integers separated by a space: ").split())
    print(f"The gcd of {a} and {b} is: {gcd(a, b)}")