import ex131
import ex130

def ev_postfix(postf):
    values = []
    for token in postf:
        if token.isnumeric():
            (values).append(int(token))
        else:
            right = values.pop()
            left = values.pop()
            result = eval(f'{left} {token} {right}')
            values.append(result)
    return values[0]

input_text = input('please type in your infix expression --- ')
tokens = ex130.num_identifier(input_text)
postfix = ex131.postfix(tokens)
print(f'Your answer is: {ev_postfix(postfix)}')
print(f'here is your postfix: {postfix}')
#3,4,+