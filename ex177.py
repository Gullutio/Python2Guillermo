def roman_to_int(roman):
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if not roman:
        return 0
    return (values[roman[1]] - values[roman[0]] + roman_to_int(roman[2:]) if len(roman) > 1 and values[roman[0]] < values[roman[1]] 
            else values[roman[0]] + roman_to_int(roman[1:]))

if __name__ == "__main__":
    roman = input("Enter a Roman numeral: ").strip().upper()
    print(f"The integer value of {roman} is: {roman_to_int(roman)}")