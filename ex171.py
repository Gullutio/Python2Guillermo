import sys

MAX_LINE_LENGTH = 50

def format_file(file_path, line_length):
    try:
        with open(file_path) as f:
            paragraphs = f.read().replace('\n', ' ').split('  ')
        for p in paragraphs:
            line, length = '', 0
            for word in p.split():
                if length + len(word) + 1 > line_length:
                    print(line)
                    line, length = '', 0
                line += (' ' if line else '') + word
                length += len(word) + 1
            if line: print(line)
            print()
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 <script.py> <file>")
        sys.exit(1)
    format_file(sys.argv[1], MAX_LINE_LENGTH)

if __name__ == "__main__":
    main()
