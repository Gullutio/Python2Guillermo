
def precedence(op):
    if op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/":
        return 2
    elif op.isnumeric():
        return 3
    elif op == "^":
        return 4
    else:
        return -1
if __name__ == "__main__":       
    operator = input("type in an operator")
    print(precedence(operator))
