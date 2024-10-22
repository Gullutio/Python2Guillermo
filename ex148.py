import random
import ex147, ex146_a
def create_calls():
    calls = []
    ranges = {'b':(1,15),
              'i':(16,30),'n':(31,45),'g':(46,60),'o':(61,75)}
    for letter, (start, end) in ranges.items():
        for num in range(start, end+1):
            calls.append(f'{letter}{num}')
    return calls

def mark_nums(card,call):
    letter = call[0]
    number = int(call[1:])

    if letter in card:
        for i, num in enumerate(card[letter]):
            if num == number:
                card[letter][i] = 0
                return True
    return False

def sim_game():
    card = ex146_a.bingo_creator()
    calls = create_calls()
    random.shuffle(calls)

    calls_made = 0
    for call in calls:
        calls_made += 1
        if mark_nums(card, call):
            if ex147.is_winning(card):
                #print(ex146_a.bingo_format(card)) TEST
                return calls_made
            
if __name__ == '__main__':
    results = []
    for game in range(1000):
        calls = sim_game()
        results.append(calls)
    print(f' After 1000 games here are the stats: minimum:{min(results)}, maximum:{max(results)}, average: {sum(results)/len(results)} ')