import random


def generate_code(length):
    return "".join(str(random.randint(0, 9)) for _ in range(length))


def generate_codes(num_codes, min_length, max_length):
    return [
        generate_code(random.randint(min_length, max_length)) for _ in range(num_codes)
    ]


if __name__ == "__main__":
    num_codes_to_generate = 10  # You can change this number as needed
    min_code_length = 10
    max_code_length = 12

    generated_codes = generate_codes(
        num_codes_to_generate, min_code_length, max_code_length
    )

    print("Generated Codes:")
    for code in generated_codes:
        print(code)
