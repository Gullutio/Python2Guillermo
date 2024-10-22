print('selects who you wanna call')
contacts = {'shark baby': 335618793, 'willie the wolf': 222222222,
            'mom': 97233737, 'dad': 45678201, 'unknown': 'unknown number'}

call = input(contacts)

print(f'calling {call} at {contacts[call]} ')
