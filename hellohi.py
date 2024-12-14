



import sys

try:
    in_single = False
    in_double = False
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file,'r') as infile:
        with open(output_file,'w') as outfile:
            for line in infile:
                clean =''
                for char in line:

                    if char == "'" and not in_double:
                        in_single = not in_single
                    elif char == '"' and not in_single:
                        in_double = not in_double
                    elif char == '#' and not in_single and not in_double:
                        print(char)
                        break


                    clean += char
                    a = "hello # bye"
                outfile.write(clean.rstrip()+'\n')



    print(f'the name of your new file - {output_file}')

except FileExistsError as e:
    print('oops there was an error - {e}')
