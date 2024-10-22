def dupe_delete():
    input_text = ""
    wordlist = []
    while input_text != "0":
        input_text = input("type in a word")

        if input_text in wordlist:
            continue

        else:
            wordlist.append(input_text)
    wordlist.pop(len(wordlist) - 1)
    return wordlist


print(dupe_delete())
