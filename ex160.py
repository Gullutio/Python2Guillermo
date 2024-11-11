import sys
follows_rule = set()
violates_rule = set()

try:
    with open(sys.argv[1],'r') as file:
        for line in file:
            words = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in line).split()
            
            for word in words:
                word = word.lower()
                ie_index = word.find('ie')
                ei_index = word.find('ei')
                
                if ie_index >= 0:
                    if ie_index > 0 and word[ie_index - 1] == 'c':
                        violates_rule.add(word)
                    else:
                        follows_rule.add(word)
                elif ei_index >= 0:
                    if ei_index > 0 and word[ei_index - 1] == 'c':
                        follows_rule.add(word)
                    else:
                        violates_rule.add(word)

    print(f"follows: {follows_rule} violates: {violates_rule}")

except FileNotFoundError:
    print("File not found")
