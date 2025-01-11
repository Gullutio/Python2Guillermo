def v_t():
    final = 0
    while True:
        input_text = input('Type in a number : ')
        if input_text == '':
            break
        try:
            final += float(input_text)
        except ValueError:
            print("invalid.")
    return final

result = v_t()
