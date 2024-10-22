def num_identifier(tokens):
    last_tok = ''
    final_tokens = []

    for token in tokens:
        if (token == '+' or token == '-') and not last_tok.isnumeric():
            final_tokens.append('u' + token)
        else:
            final_tokens.append(token)
        last_tok = token
    return final_tokens

def unifier(numid):
    ine = 0
    for val in numid:
        ine += 1
        if 'u' in val:
             numid[ine].append(val.pop())
if __name__ == "__main__":       
    print(num_identifier(['-','3'])) #<--- put yout test cases here
    print(unifier(unifier(num_identifier('2','+','+','3','-','8','*','300','*','-','10',''))))