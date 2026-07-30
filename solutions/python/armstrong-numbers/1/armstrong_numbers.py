def is_armstrong_number(number):
    sum_digit = 0
    digits_str = str(number)
    raised_power = len(digits_str)
    for digit in digits_str:
        sum_digit += int(digit) ** raised_power
    return sum_digit == number
