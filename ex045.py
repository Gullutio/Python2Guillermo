print('hi wassup im chess bot')
input_text = input(
    'Please type in the chess piece u want me to analyse example: c1: ')
pieces = {'b8': 'black', 'd8': 'black', 'f8': 'black', 'h8': 'black', 'a7': 'black', 'c7': 'black', 'e7': 'black', 'g7': 'black', 'b6': 'black', 'd6': 'black', 'f6': 'black', 'h6': 'black', 'a5': 'black', 'c5': 'black', 'e5': 'black', 'g5': 'black',
          'b4': 'black', 'd4': 'black', 'f4': 'black', 'h4': 'black', 'a3': 'black', 'c3': 'black', 'e3': 'black', 'g3': 'black', 'b2': 'black', 'd2': 'black', 'f2': 'black', 'h2': 'black', 'a1': 'black', 'c1': 'black', 'e1': 'black', 'g1': 'black', 'a8': 'white', 'c8': 'white', 'e8': 'white', 'g8': 'white', 'b7': 'white', 'd7': 'white', 'f7': 'white', 'h7': 'white', 'a6': 'white', 'c6': 'white', 'e6': 'white', 'g6': 'white', 'b5': 'white', 'd5': 'white', 'f5': 'white', 'h5': 'white', 'a4': 'white', 'c4': 'white', 'e4': 'white', 'g4': 'white', 'b3': 'white', 'd3': 'white', 'f3': 'white', 'h3': 'white', 'a2': 'white', 'c2': 'white', 'e2': 'white', 'g2': 'white', 'b1': 'white', 'd1': 'white', 'f1': 'white', 'h1': 'white'}

try:
    print(f'That square is {pieces[input_text]}.')

except:
    print('Sorry thats not a valid chess square.')
