import random

def roller():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

frequency = {total: 0 for total in range(2, 13)}

for i in range(1000):
    total = roller()
    frequency[total] += 1

expected_percentages = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

print(f"{'Total':<6} {'Simulated Percent':<20} {'Expected Percent':<20}")
for total in range(2, 13):
    simulated_percent = (frequency[total] / 1000) * 100
    expected_percent = expected_percentages[total]
    print(f"{total:<6} {simulated_percent:<20.2f} {expected_percent:<20.2f}")