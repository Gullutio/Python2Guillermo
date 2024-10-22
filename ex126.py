import ex125
def deal(hands, cards, deck):
    dealt = []
    final = ''
    for k in range(hands):
        dealt.append(deck.pop(-1))
    item = 0
    for i in range((cards - 1) * hands):
        dealt[item] += f', {(deck.pop(-1))}'
        item += 1
        if item == hands:
            item = 0
    for hand in range(hands):
        final = final + f'{dealt[hand - 1]}\n'
    return f'\nYour hands:\n{final}\nYour remaining cards: \n{deck}'

hands = int(input('how many hands do u want?'))
cper_hand = int(input('how many cards per hand do you want.'))
deck = ex125.shuffle(ex125.create_deck())
print(deal(hands, cper_hand, deck))