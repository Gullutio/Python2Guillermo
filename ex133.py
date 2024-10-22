def str_replacer(rep):
    return "".join([str(i) for i in rep])

def isSublist(larger, smaller):  
    return str_replacer(smaller) in str_replacer(larger)

large = [1,2,3,4]
small = [1]
sub_or_not = isSublist(large,small)  
if sub_or_not == True:
    print(f'The sublist {small} fits into the list {large} ')
else:
    print(f'The sublist {small} does not fit into the list {large} ')

    