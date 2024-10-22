import random

def shuffle(card):
    shuffled = []
    for s in range(len(card)):
        r = random.randint(0, 51 - s)
        shuffled.append(card.pop(r))
    return shuffled  

def create_deck():  
    cards = []
    suit_av = "scdh"#works both <<|
    #suit_av = ["s", "c", "d", "h"]
    value_av = "J2TAQK3456789" #works both <<|
    #value_av = ["J", "2", "T", "A","Q","K", "3","4","5","6","7","8","9"]

    for suit in suit_av:
        for value in value_av:
            cards.append(value + suit)
    return cards

if __name__ == "__main__":
    finaldeck = create_deck()
    print(f'Your unshuffled list is: {finaldeck}\n\nYour shuffled list is: {shuffle(finaldeck)}')
