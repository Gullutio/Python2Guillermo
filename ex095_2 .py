initial_val = input(
    "Hi, type in a non capitalized sentence, Ill capitalize it for you!"
)
processed_val = initial_val.capitalize()


def capitalizer(initial, processed):
    processed_2 = ""
    i_count = 0
    index = 0
    last_char = ""
    cap = False

    for i in processed:
        if i == "i":
            i_count += 1
        if i == "i" and processed[index + 1] == " " and last_char == " ":
            processed = processed.replace(i, i.upper(), i_count)
            processed_2 += processed[index]
        else:
            processed_2 += processed[index]
        if (
            cap == True
            and last_char == " "
            or last_char == "."
            or last_char == "?"
            or last_char == "!"
        ):
            processed_2 = processed_2.replace(i, i.upper())
            cap = False
            if processed[index] == " ":  # something here
                cap = True
            # processed = processed.replace(i, i.upper(), i_count)
        last_char = i
        index += 1
    print(processed_2)


capitalizer(initial_val, processed_val)
# and last_char == " "
# or cap == True
# create a new string
# for each character add the character into the new string
# this character can be modified based on the capitalization rules.
# this gives me more control than .replafe and I canq then print the new string
