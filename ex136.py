def reverseLookup(this_dict, search):
        final = []
        for key in this_dict:
            if search == this_dict[key]:
                final.append(key)
        return final
            

input_text = input('please type in the value you wnat to search for')
dictionary = {'a':'9',
              'b':'60',
              'c':'2',# dictionary = {KEYS:VALUES}
                        # ask for keys: values
              'd':'1',
              'e':'9',
            'f': '13'}
print(reverseLookup(dictionary, input_text))