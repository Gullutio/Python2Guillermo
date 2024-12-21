import sys

def find_words_with_vowels(file_path):
    try:
        with open(file_path) as f:
            words = f.read().splitlines()
        vowels = "aeiouy"
        for word in words:
            w = word.lower()
            if all(v in w for v in vowels) and w.find(vowels) != -1:
                print(word)
    except FileNotFoundError:
        print(f"error {file_path} not found.")
    except Exception as e:
        print(f"error {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 <script.py> <file>")
        sys.exit(1)
    find_words_with_vowels(sys.argv[1])

if __name__ == "__main__":
    main()
