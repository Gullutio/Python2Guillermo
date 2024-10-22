import ex117

a_string = input("Type in a sentence - ")
indexer = ex117.word_findr(a_string)
first = a_string
left = 0
right = len(indexer) - 1
while left <= right:
    if indexer[left] != indexer[right]:
        print("its not a palindrome")
        quit()
    elif indexer[left] == indexer[right]:
        left += 1
        right -= 1

print("its a palindrome")
