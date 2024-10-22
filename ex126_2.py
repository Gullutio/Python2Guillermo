import ex125

def deal(hands, cards, deck):
    dealt = []
    for k in range(hands):
        dealt.append([])

    for i in range(cards * hands):
        dealt[i%hands].append(deck.pop())
    return dealt

hands = int(input('how many hands do u want?'))
cper_hand = int(input('how many cards per hand do you want.'))
deck = ex125.shuffle(ex125.create_deck())
print(f'Your hands: {deal(hands, cper_hand, deck)} \n\nYour remaining cards:{deck}')