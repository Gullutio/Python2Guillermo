def translator(input_text):
    if input_text[0] in vow:
        return input_text + "way"
    else:
        for i in range(len(input_text)):
            if input_text[i] in vow:
                if input_text[0].isupper():
                    return input_text[i:].capitalize() + input_text[:i].lower() + "ay"
                else:
                    return input_text[i:] + input_text[:i] + "ay"

vow = "aeiouAEIOU"
input_text = input("Type in a sentence: ")
wordlist = input_text.split()
final = ""
for word in wordlist:
    final += translator(word) + " "
print(final.strip())
