def num_identifier(tokens):
    last_tok = ''
    final_tokens = []
    next = ''
    
    for token in tokens:
        if (token == '+' or token == '-') and not last_tok.isnumeric():
            next = token
        elif next != '':
            final_tokens.append(next + token)
            next = ''
        else:
            final_tokens.append(token)
        last_tok = token
    return final_tokens

if __name__ == "__main__":       
    print(num_identifier(['-','3'])) #<--- put yout test cases here
    print(num_identifier(['2','+','+','3','-','8','*','300','*','-','10',''])) #<--- put yout test cases here