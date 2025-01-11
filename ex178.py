def is_palindrome_recursive(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

def main():
    user_input = input("input text for palindore -  ").strip()
    if is_palindrome_recursive(user_input):
        print(f'"{user_input}" is a palindrome!')
    else:
        print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    main()