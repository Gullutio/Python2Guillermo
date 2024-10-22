try:
    #file = open('ex149.txt')
    #for i in range(10):
     #   print(file.readline())
    #file.close()
    with open('ex149.txt') as file:
        for i in range(10):
            print(file.readline())

except FileNotFoundError:
    print(f'are you sure that the file exists?')
