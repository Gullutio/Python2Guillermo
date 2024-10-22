import ex130
import ex097

def postfix(tokens): #-----> returns list
    postf = []
    operators = []

    for token in tokens:
        if token.isnumeric():
            postf.append(token)
        elif ex097.precedence(token) != -1 and ex097.precedence(token) != 3:        
            while operators != [] and operators[-1] != '(' and ex097.precedence(token) < ex097.precedence(operators[-1]): 
                postf.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                postf.append(operators.pop())
            operators.pop()

    while operators != []:
        postf.append(operators.pop())
    return postf

if __name__ == "__main__":  
    input_text = input('type in your infix pls ----> ')
    tokens = ex130.num_identifier(input_text)
    print(postfix(tokens))