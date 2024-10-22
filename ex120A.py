def formatter(form_sentence):
    form_sentence[-1] = form_sentence[-1].replace(",", "")
    if len(form_sentence) > 1:
        form_sentence[-2] = form_sentence[-2].replace(",", " and ")
    return "".join(form_sentence)


form_sentence = []
input_text = ""
while True:
    input_text = input("Type in a word")
    if input_text == "":
        break
    else:
        input_text = input_text + ","
        form_sentence.append(input_text)

print(formatter(form_sentence))
