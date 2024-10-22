import random as r
def bingo_creator():
    b_list = []
    i_list = []
    n_list = []
    g_list = []
    o_list = []
    bingo_card  = {'b':b_list , 'i':i_list,  'n':n_list, 'g':g_list, 'o':o_list,}
    first = 1
    second = 15
    for char in bingo_card:
        for _ in range(5):
            bingo_card[char] += [r.randint(first,second)]
        first = second +1
        second += 15
    return bingo_card

def bingo_format(card):
    rows = []
    rows.append("B   I   N   G   O")
    for i in range(5):
        row = [str(card[char][i]).rjust(2) for char in 'bingo']
        rows.append("  ".join(row))
    return "\n".join(rows)

if __name__ == "__main__":
    import random as r
    bingo_card = bingo_creator()
    print(bingo_format(bingo_card))