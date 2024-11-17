import os

try:
    def read_names(gender):
        BABYNAMES_PATH = os.path.join(os.curdir, 'BabyNames')
        names = {}
        for file_name in os.listdir(BABYNAMES_PATH):
            if gender in file_name:
                with open(os.path.join(BABYNAMES_PATH, file_name), 'r') as f:
                    #print(file_name)
                    #print(f.readline())
                    line = f.readline().strip()
                    if line:
                        print(line.strip("0123456789"))
                        name = line.strip("0123456789")
                        if name in names:
                            names[name] += 1
                        else:
                            names.update({name:1})
                        
                        
                        #names.add(name)
        return names

    def display_popular_names():
        girls_names = sorted(read_names('Girls'))
        boys_names = sorted(read_names('Boys'))
        print(f'Most popular girls names:{girls_names}')
        print(f"\nMost popular boys' names:{boys_names}")

    print(display_popular_names())
   #read_names('')
except FileNotFoundError as e:
    print(f"Oops, I think there is a problem :( - {e}")

