import sys

try:
    if len(sys.argv) < 2:
        print("oops: Missing file name.")
        sys.exit(1)


    prev_word = ''
    line_number = 0

    with open(sys.argv[1], "r") as user_file:
        for line in user_file:
            line_number += 1
            words = line.strip().split()
            for word in words:
                clean_word = ''.join(char for char in word if char.isalnum() or char == "'").lower()
                if clean_word and clean_word == prev_word:
                    print(f"Repeated word '{clean_word}' found on line {line_number}")
                prev_word = clean_word

except FileNotFoundError as e:
    print(f"oops: {e}")

except Exception as e:
    print(f"oops: An unexpected error occurred: {e}")
