nato_alphabet = {
    'A': "Alpha", 'B': "Bravo", 'C': "Charlie", 'D': "Delta", 'E': "Echo",
    'F': "Foxtrot", 'G': "Golf", 'H': "Hotel", 'I': "India", 'J': "Juliett",
    'K': "Kilo", 'L': "Lima", 'M': "Mike", 'N': "November", 'O': "Oscar",
    'P': "Papa", 'Q': "Quebec", 'R': "Romeo", 'S': "Sierra", 'T': "Tango",
    'U': "Uniform", 'V': "Victor", 'W': "Whiskey", 'X': "X-ray", 'Y': "Yankee", 'Z': "Zulu"
}

def phonetic_spelling(word):
    word = word.upper()
    if not word:
        return ""
    first_letter = word[0]
    if first_letter in nato_alphabet:
        return nato_alphabet[first_letter] + ' ' + phonetic_spelling(word[1:])
    else:
        return phonetic_spelling(word[1:])

if __name__ == "__main__":
    user_input = input("enter a word: ").strip()
    result = phonetic_spelling(user_input).strip()
    print(f"phonetic: {result}")
