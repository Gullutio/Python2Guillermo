def checker(password):
    uppercase = False
    lowercase = False
    number = False
    length = False
    if len(password) < 8:
        return False
    else:
        for i in password:
            if i.isupper() == True:
                uppercase = True
            if i.islower() == True:
                lowercase = True
            if i.isnumeric() == True:
                number = True
            if len(password) >= 8:
                length = True
    if uppercase == True and lowercase == True and number == True and length == True:
        return True
    else:
        return False


if __name__ == "__main__":
    input_text = input("type in an 8 character password --- ")
    if checker(input_text) == True:
        print("good password")
    else:
        print("bad password")
