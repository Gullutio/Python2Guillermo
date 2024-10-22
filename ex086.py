distance = float(input("how many km have you travelled?"))


def fare(d):
    m = d * 1000
    fee = ((m // 140) * 0.25) + 4
    return f"Your taxi ride willl cost {fee}$"


print(fare(distance))
