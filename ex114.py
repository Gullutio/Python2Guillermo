def orderer():
    finished_list = []
    holder_list = []
    input_text = " "
    while input_text != "":
        last = input_text
        input_text = input("type in a number pls")
        if last[0] == "-" or input_text[0] == "-":
            holder_list.append(input_text)
            print(holder_list)
        else:
            finished_list.append(input_text)
            print(finished_list)
        holder_list = [holder_list.append(input_text.strip("-"))]
        holder_list = [input_text.replace("-", " ")]
        holder_list.sort
        holder_list = [i.replace(" ", "-") for i in holder_list]
        print(holder_list)


orderer()
