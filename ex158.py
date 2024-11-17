# JU: 
# - needs to read the name of output file as well.
# - need to output to file, not print
# - fix the code to fulfill the requirementss
import sys

try:
    final = ''
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file,'r') as infile:
        with open(output_file,'w') as outfile:
            for line in infile:
                clean = line.split('#')[0].rstrip()
                outfile.write(clean+'\n')

    print(f'the name of your new file - {output_file}')

except:
    print('oops there was an error')