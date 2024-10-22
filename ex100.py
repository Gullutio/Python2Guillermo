# LETS GOOOOOOOO EXERCISE #100
# us eth chr function - acts as ascii table
# research random module
import random as r


def generator(chars):
    for i in range(r.randint(7, 10)):
        chars += chr(r.randint(33, 126))
    return chars


# print(f"your current password is: {generator(characters)}")
if __name__ == "__main__":
    characters = ""
    print(generator(characters))
