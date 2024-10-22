import ex115

print("perfect number:")
for i in range(1, 10000):
    if sum(ex115.divisorer(i)) == i:
        print(i)
