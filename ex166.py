import os
import sys

def collect_names(data_path):

    boys_names, girls_names = set(), set()
    for file_name in os.listdir(data_path):
        if file_name.endswith('.txt'):
            target_set = None

            if "BoysNames" in file_name:
                target_set = boys_names
            elif "GirlsNames" in file_name:
                target_set = girls_names
            if target_set != None:
                with open(os.path.join(data_path, file_name), 'r') as f:
                    for line in f:
                        name = line.rsplit(' ',1)[0].strip()
                        target_set.add(name)

    return boys_names, girls_names
    

def main():
    if len(sys.argv) > 1:
        print("oops incorrect value")
        return

    data_path = os.path.join(os.curdir, 'BabyNames')
    if not os.path.isdir(data_path):
        print(f"Invalid directory: {data_path}")
        return

    boys_names, girls_names = collect_names(data_path)
    print(" Boys' Names:", sorted(boys_names))
    print("\n Girls' Names:", sorted(girls_names))

if __name__ == "__main__":
    main()
