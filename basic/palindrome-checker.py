def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
number = 17  # Replace this with any number you want to check
print(f"Is {number} a prime number? {is_prime(number)}")
