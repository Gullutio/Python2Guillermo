import sys
import string

try:
    with open(sys.argv[1], 'r') as file:
        def read_words():
            translator = str.maketrans('', '', string.punctuation)
            words = file.read().translate(translator).lower().split()
            return words

        def analyze_proportions(words):
            letter_counts = {letter: 0 for letter in string.ascii_lowercase}
            total_words = len(words)

            for word in words:
                for letter in set(word):
                    if letter in letter_counts:
                        letter_counts[letter] += 1

            if total_words == 0:
                return None, None
            
            proportions = {letter: count / total_words for letter, count in letter_counts.items()}
            smallest_letter = min(proportions, key=proportions.get)
            return proportions, smallest_letter

        words = read_words()
        proportions, smallest_letter = analyze_proportions(words)

        if proportions is None:
            print("The file contains no words.")
        else:
            for letter, proportion in sorted(proportions.items()):
                print(f"{letter}: {proportion:.2%}")
            print(f"\nleast used letter: {smallest_letter}")

except FileNotFoundError as e:
    print(f"Oops, there’s a problem :{e}")