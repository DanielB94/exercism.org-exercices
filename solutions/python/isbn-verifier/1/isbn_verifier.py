def is_valid(isbn):
    clean_isnb = isbn.replace('-', '')

    if len(clean_isnb) != 10: return False
    clean_digits = list(clean_isnb)
    if clean_digits[-1] in ('X', 'x'): clean_digits[-1] = '10' # str to handler the for properly

    if not all(clean_digit.isnumeric() for clean_digit in clean_digits):
        return False
    digits = [int(digit) for digit in clean_digits]

    total = sum(digit * (10 - i) for i, digit in enumerate(digits))

    return total % 11 == 0

    
