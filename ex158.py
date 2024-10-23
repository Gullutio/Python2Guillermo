# JU: 
# - needs to read the name of output file as well.
# - need to output to file, not print
# - fix the code to fulfill the requirementss

input_text = input('type in name of input file - ')
final = ''
with open(input_text,'r') as file:
    lines = file.readlines()
    for line in lines:
        if '#' in line:
            count = 0
            for char in line:
                count += 1
                #print(char, count)
                if char == '#':
                    final = line[:count]
                    final = final.replace('#','')
                    print(final)
        else:
            print(line)
        