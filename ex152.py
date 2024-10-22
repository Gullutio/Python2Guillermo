try:
    file = open("ex150.txt", "r")
    #f_len = len(file)
    index = 0
    for char in file:
        index += 1
        print(f'{index}: {char}')
except:
    print('sorry there was an error with your file')
