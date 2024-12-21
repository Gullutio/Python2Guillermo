import sys, os

def find_missing_comments(file_path):
    results = []
    try:
        lines = open(file_path).readlines()
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (i == 0 or not lines[i-1].strip().startswith('#')):
                results.append((line.split('(')[0][4:].strip(), i + 1))
    except FileNotFoundError:
        print(f" cant open {file_path}.")
    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 <script.py> <file1> [<file2> ...]")
        sys.exit(1)

    for file_path in sys.argv[1:]:
        if not os.path.isfile(file_path):
            print(f" {file_path} not found.")
            continue

        for func, line in find_missing_comments(file_path):
            print(f"file: {file_path}, line: {line}, function: {func}")

if __name__ == "__main__":
    main()
