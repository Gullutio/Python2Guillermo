# JU:
# - resolt needs to include capitalization of the second word. Currently, it does not.
# - algorithm is too long. Currently, it filters words of length greater than 3.
# - fix with shorter algorithm to fulfill the same requirements.

import random as r
import sys
try:
    #ex150.txt
    with open(sys.argv[1],'r') as file:
        words = []
        for word in file:
            if len(word.strip()) >= 3:
                words.append(word.strip())
        while True:
            w1 = r.choice(words)
            w2 = r.choice(words)
            if 8 <= len(w1) + len(w2) and len(w1) + len(w2)  <= 10:
                print((w1+w2).capitalize())
                break
except FileNotFoundError:
    print('oops we could not find your file!')