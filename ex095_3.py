def capitalizer(sentence):
    sentence = sentence.capitalize() + "i"
    result = ""
    i_count = 0
    index = 0
    last_char = ""
    cap = False

    for i in sentence:
        if i == "i":
            i_count += 1
        if index + 1 < len(sentence):
            if (
                cap == True
                and last_char == " "
                or last_char == "."
                or last_char == "?"
                or last_char == "!"
            ):
                result += sentence[index].upper()
                cap = False

                if sentence[index] == " ":
                    cap = True

            elif (
                i == "i"
                and last_char == " "
                and (
                    sentence[index + 1] == " "
                    or sentence[index + 1] == "'"
                    or sentence[index + 1] == "."
                    or sentence[index + 1] == "!"
                    or sentence[index + 1] == "?"
                )
            ):
                result += sentence[index].upper()

            else:
                result += i
        last_char = i
        index += 1
    return result


initial_val = input(
    "Hi, type in a non capitalized sentence, Ill capitalize it for you!"
)

print(capitalizer(initial_val))
# and last_char == " "
# or cap == True
# create a new string
# for each character add the character into the new string
# this character can be modified based on the capitalization rules.
# this gives me more control than .replafe and I canq then print the new string
