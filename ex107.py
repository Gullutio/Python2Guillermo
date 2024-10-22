def reducer(n, d):
    gcf = 0

    if n < d:
        gcf = n
    elif d == 0 or n == 0:
        return "invalid value"
    else:
        gcf = d

    while d % gcf != 0 or n % gcf != 0:
        gcf = gcf - 1
    final = f"{n / gcf}/{d / gcf}"

    return final


numerator = int(input("type in your first number"))
denominator = int(input("type in your second number"))
print(reducer(numerator, denominator))
# Fix error ^^^^^^^^^ 100 - 10
