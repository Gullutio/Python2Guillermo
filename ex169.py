import sys
import re

try:
    if len(sys.argv) < 4:
        print('Usage: python3 <script.py> <original_file> <sensitive_words_file> <redacted_file>')
        sys.exit(1)

    def load_sensitive_words(filename):
        with open(filename, "r") as file:
            words = []
            for line in file:
                words.extend(line.strip().split())
            return words

    def redact_text(text, sensitive_words):
        for word in sensitive_words:
            pattern = re.compile(re.escape(word), re.IGNORECASE)  #re.ignorecase ignores capitalization
            text = pattern.sub('*' * len(word), text)  
        return text
    
    original_file = sys.argv[1]
    sensitive_words_file = sys.argv[2]
    redacted_file = sys.argv[3]
    sensitive_words = load_sensitive_words(sensitive_words_file)

    with open(original_file, "r") as infile, open(redacted_file, "w") as outfile:
        for line in infile:
            redacted_line = redact_text(line, sensitive_words)
            outfile.write(redacted_line)

    print(f'Redacted file saved as: {redacted_file}')

except FileNotFoundError as e:
    print(f'Error: {e}')
