def word_findr(input):
    word_list = []
    word = ""
    for count, i in enumerate(input):
        if (
            i == "."
            or i == "!"
            or i == "?"
            or i == ","  # a' 'a
            or i == ";"
            or i == ":"
            or i == "'"
        ):
            if count != 0 and count + 1 < len(input):
                if input[count - 1].isalpha() and input[count + 1].isalpha():
                    word += i
        elif i == " ":
            word_list.append(word)
            word = ""
        else:
            word += i
    word_list.append(word)
    for i in range(word_list.count("")):
        word_list.remove("")
    return word_list


if __name__ == "__main__":
    input_text = input("type in a sentence - ")
    print(f"Your final list is: {word_findr(input_text)}")
