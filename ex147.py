#{'b': [0, 6, 9, 8, 15], 'i': [0, 20, 26, 21, 27], 'n': [0, 34, 44, 36, 39], 'g': [0, 51, 60, 51, 50], 'o': [0, 71, 68, 64, 66]} HORIZONTAL
#{'b': [0, 6, 9, 8, 15], 'i': [27, 0, 26, 21, 27], 'n': [34, 34, 0, 36, 39], 'g': [59, 51, 60, 0, 50], 'o': [72, 71, 68, 64, 0]} DIAGONAL 1
#{'b': [12, 6, 9, 8, 0], 'i': [27, 20, 26, 0, 27], 'n': [34, 34, 0, 36, 39], 'g': [59, 0, 60, 51, 50], 'o': [0, 71, 68, 64, 66]} DIAGONAl 2
#{'b': [12, 6, 9, 8, 15], 'i': [27, 20, 26, 21, 27], 'n': [34, 34, 44, 36, 39], 'g': [59, 51, 60, 51, 50], 'o': [0, 0, 0, 0, 0]} VERTICAL

def is_winning(card):
    for letter in 'bingo':
        sum = 0
        for i in range(5):
            sum += card[letter][i]
        if sum == 0:
            return True #VERTICAL
    sum = 0 
    for b in range(5):
        for letter in 'bingo':
            sum += card[letter][b]
        if sum == 0:
            return True #HORIZONTAL
    sum = 0 
    for c in range(5):
        letter = 'bingo'[c]
        sum += card[letter][c]
        if sum == 0:
            return True #DIAGONAL CASE #1
    sum = 0
    for d in range(5):
        letter = 'bingo'[d]
        sum += card[letter][4-d]
    if sum == 0:
        return True #DIAGONAL CASE#2
    
    return False # IF NONE RETURN FALSE

if __name__=='__main__':
    b1 = {'b': [12, 6, 9, 8, 0], 'i': [27, 20, 26, 0, 27], 'n': [34, 34, 0, 36, 39], 'g': [59, 0, 60, 51, 50], 'o': [0, 71, 68, 64, 66]}
    b2 = {'b': [0, 6, 9, 8, 15], 'i': [27, 0, 26, 21, 27], 'n': [34, 34, 0, 36, 39], 'g': [59, 51, 60, 0, 50], 'o': [72, 71, 68, 64, 0]}
    b3 = {'b': [12, 6, 9, 8, 0], 'i': [27, 20, 26, 0, 27], 'n': [34, 34, 0, 36, 39], 'g': [59, 0, 60, 51, 50], 'o': [0, 71, 68, 64, 66]}
    b4 = {'b': [12, 6, 9, 8, 15], 'i': [27, 20, 26, 21, 27], 'n': [34, 34, 44, 36, 39], 'g': [59, 51, 60, 51, 50], 'o': [0, 0, 0, 0, 0]}
    b5 = {'b': [12, 6, 9, 8, 15], 'i': [27, 20, 26, 21, 27], 'n': [34, 34, 44, 36, 39], 'g': [59, 51, 60, 51, 50], 'o': [0, 0, 0, 0, 66]}

    print(f'{b1} {is_winning(b1)}')
    print(f'{b2} {is_winning(b2)}')
    print(f'{b3} {is_winning(b3)}')
    print(f'{b4} {is_winning(b4)}')
    print(f'{b5} {is_winning(b5)}')
    #for letter in 'bingo':
     #   real_bingo[letter][0] = 0 #HORIZ TEST
    
    #for i in range(5):
    #    for letter in 'bingo': 
     #       real_bingo[letter][i] #D
    
    #for i in range(5):
     #   for letter in 'bingo': 
      #      real_bingo[letter][abs(4-i)]

