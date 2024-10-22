initial_val = input(
    "Hi, type in a non capitalized sentence, Ill capitalize it for you!"
)
processed_val = initial_val.capitalize()


def capitalizer(initial, processed):
    index = 0
    last_char = ""
    cap = False
    for i in processed:
        print(i)
        print(cap)
        if (
            cap == True
            and last_char == " "
            or last_char == "."
            or last_char == "?"
            or last_char == "!"
        ):
            processed = processed.replace(i, i.upper())
            print(processed)
            cap = False
            if processed[index] == " ":  # something here
                cap = True
        last_char = i

        # if last_char == " " and i == "i":
        #    processed = processed.replace(i, i.upper())
        #    print(processed)
        index += 1


capitalizer(initial_val, processed_val)
# and last_char == " "
# or cap == True
