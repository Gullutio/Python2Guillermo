try:
    file = open('ex149.txt', 'r')
    lines = file.readlines()
    start_index = max(0, len(lines) - 10)
    for line in lines[start_index:]:
        print(line, end='')
        
except FileNotFoundError:
    print('file not found.')

file.close()