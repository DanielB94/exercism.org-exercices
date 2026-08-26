def sum_of_multiples(limit, multiples):
    return sum({multiple for numbers in multiples if numbers > 0 for multiple in range(numbers, limit, numbers)})
