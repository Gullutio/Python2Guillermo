import sys
try:
    with open(sys.argv[1],'r') as file:
        def read_info():
            element = {}
            for line in file:
                key, value, symbols = line.split(',',maxsplit =2)
                element[int(key)] = (symbols.replace('\n', ''), value.replace('\n', ''))
            return element
        
        def get_input(element):
            input_text = ' '
            while input_text != '':
                input_text = input('please type in an element or number - ')
                try:            
                    if input_text.isnumeric():
                        number = int(input_text)
                        if number in element:
                            symbol, name = element[number]
                            print(number, symbol, name)
                    else:
                        input_text = input_text.strip()
                        for number, (symbol, name) in element.items():
                            if input_text.lower() == symbol.lower() or input_text.lower == name.lower:
                                print(number, symbol, name)       
                                break
                except:
                    continue
        print(get_input(read_info()))

except FileNotFoundError as e:
    print(f'Oops I think theres a problem :( -  {e}')