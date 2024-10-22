def str_replacer(rep):
    final = ''
    for i in rep:
        if i != '[' and i != ']' and i != ',':
            final += i  
    return final  

def isSublist(larger, smaller):
    larger = str(larger)
    smaller = str(smaller)
    if str_replacer(smaller) in str_replacer(larger):
        return True
    else:
        return False

large = [1, 2, 3, 4]
small = [2, 3, 4]
sub_or_not = isSublist(large, small)
if sub_or_not:
    print(f'The sublist {small} fits into the list {large}')
else:
    print(f'The sublist {small} does not fit into the list {large}')