def sublist(list):
    n = len(list)
    sublist = []
    for start in range(n): 
        for end in range(start + 1, n + 1):
            sublist.append(list[start:end])
        return sublist
    
og_list = [1,2,3,4]
other_sublists = sublist(og_list)
print(other_sublists)
