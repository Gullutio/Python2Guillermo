import os
import sys

def get_top_name(file_path):
    with open(file_path, 'r') as f:
        name, count = f.readline().strip().rsplit(' ', 1)
        return name, int(count)

def get_most_popular_names(start_year, end_year):
    boys_top, boys_count = None, 0
    girls_top, girls_count = None, 0
    for year in range(start_year, end_year + 1):
        for gender, top_name, max_count in [
            ('BoysNames', boys_top, boys_count),
            ('GirlsNames', girls_top, girls_count),
        ]:
            file = os.path.join('BabyNames', f"{year}_{gender}.txt")
            if os.path.exists(file):
                name, count = get_top_name(file)
                if count > max_count:
                    if gender == 'BoysNames':
                        boys_top, boys_count = name, count
                    else:
                        girls_top, girls_count = name, count
    return boys_top, boys_count, girls_top, girls_count

def main():
    if len(sys.argv) != 3:
        print("oops try again")
        return

    try:
        start_year, end_year = int(sys.argv[1]), int(sys.argv[2])
        if start_year > end_year:
            print("inavlid year values :(")
            return

        boys, boys_count, girls, girls_count = get_most_popular_names(start_year, end_year)
        print(f"Most popular boy's name: {boys} ({boys_count})")
        print(f"Most popular girl's name: {girls} ({girls_count})")
    except ValueError:
        print("Both years must be integers")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
