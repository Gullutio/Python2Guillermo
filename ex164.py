#look through the boys name file, make a dict with all the names
#check through girl names, if it matches boy names add 1 to dict value, 
#when done print the ones with a 2 as their value
import os 
import sys

try:
    b_names = set()
    gb_names = set()
    BABYNAMES_PATH = os.path.join(os.curdir, 'BabyNames')
    with open(os.path.join(BABYNAMES_PATH, f'{sys.argv[1]}_BoysNames.txt'), 'r') as boyfile:
        for line in boyfile:
            name = line.strip("0123456789")
            b_names.add(name)

    with open(os.path.join(BABYNAMES_PATH, f'{sys.argv[1]}_GirlsNames.txt'), 'r') as girlfile:
        for line in girlfile:
            name = line.strip("0123456789")
            if name in b_names:
                gb_names.add(name)
    print(f'Gender Neutral names include: {gb_names}')

except FileNotFoundError as e:
    print(f'oops file could not be found: {e}')