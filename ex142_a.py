# set
def u_chars(w1,w2):
    first = set(w1)
    second = set(w2)
    print(first,second)
    print(first.difference(second))
    if first.difference(second) == set():

        return 'its an anagram' #123 1234 = 4
    else:
        return ''
    
w1 = input('hi type in a word')
w2 = input('hi type in a word')
print(u_chars(w1,w2))