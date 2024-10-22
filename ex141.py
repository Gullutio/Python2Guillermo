def num2eng(num):
    words = []
    ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    tens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    twenties = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    hundreds = {100: 'hundred'}

    if num == 0:
        return 'zero' 

    if num >= 100:
        words.append(ones[num // 100])
        words.append(hundreds[100])
        num %= 100

    if num >= 20:
        words.append(twenties[num - (num % 10)])
        num %= 10
    
    if num >= 10:
        words.append(tens[num])
    elif num > 0:
        words.append(ones[num])

    return ' '.join(words)

input_text = input('Enter a number from 0 to 999')
try:
    number = int(input_text)
    result = num2eng(number)
    print(f"{number} in English words is: {result}")
except:
    print("Invalid")