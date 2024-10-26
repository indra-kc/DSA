def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage
print(sum_of_digits(123))   # Output: 6 (1 + 2 + 3)
print(sum_of_digits(4567))  # Output: 22 (4 + 5 + 6 + 7)
print(sum_of_digits(908))   # Output: 17 (9 + 0 + 8)
