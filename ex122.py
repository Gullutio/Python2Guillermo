input_text = input("type in a word to convert to pig latin")
holder = ""
ind = -1
if (
    input_text[0] != "a"
    or input_text[0] != "e"
    or input_text[0] != "i"
    or input_text[0] != "o"
    or input_text[0] != "u"
):
    for i in range(len(input_text)):
        print(len(input_text))
        if (
            input_text[i] == "a"
            or input_text[i] == "e"
            or input_text[i] == "i"
            or input_text[i] == "o"
            or input_text[i] == "u"
        ):
            input_text = input_text.join("ay")
            break
        else:
            holder = input_text[i]
            input_text[i].replace(input_text[i], "")
            input_text = input_text.join(holder)

            print(input_text)
