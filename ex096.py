def int_check(vals):  
    vals = vals.replace(" ", "")
    for i in vals:
        try:
            if i.isnumeric() or (vals[1].isnumeric() and vals[0] == "-" or vals[0] == "+"):
                pass
            else:
                return False
        except:
            return False
    return True

if __name__ == "__main__":       
    input_text = input("Please type in a string, ill judge if it can be an integer")
    print(int_check(input_text))
