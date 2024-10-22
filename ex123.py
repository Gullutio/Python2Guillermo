def translator(input_text):
    words = "".join(char for char in input_text if char not in punctu)
    punctuations = "".join(char for char in input_text if char in punctu)
    if words[0] in vow:
        return words + "way"
    else:
        for i in range(len(words)):
            if words[i] in vow:               
                return words[i:].capitalize() + words[:i].lower() + "ay" + punctuations


punctu = ",!?."
vow = "aeiouAEIOU"
input_text = input("Type in a sentence: ")
wordlist = input_text.split()
final = ""
for word in wordlist:
    final += translator(word) + " "

print(final.strip())
