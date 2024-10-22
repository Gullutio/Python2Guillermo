import ex100
import ex102

characters = ""


def good_pass():
    attempts = 1
    password = ex100.generator(characters)
    while ex102.checker(password) != True:
        password = ex100.generator(characters)
        attempts += 1
    return f"attempts - {attempts}, password - {password}"


print(good_pass())
