from os import system

try:
    file_1 = open("ex149.txt")
    file_2 = open("ex150.txt")
    system("cat ex149.txt ex150.txt")

except:
    print('im sorry, your files are invalid')

file_1.close()
file_2.close()