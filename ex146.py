import random as r
def bingo_creator():
    first = 1
    second = 15
    bingo_l = ['b','i','n','g','o']
    columns = {}
    for b in range(5):
        for i in range(5):
            base = {bingo_l[b]:r.randint(first,second)}
            columns.update(base)
            print(columns)
            base = {}
        first = second + 1
        second += 15
print(bingo_creator())