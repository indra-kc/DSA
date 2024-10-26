def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Example usage
n = 10  # Replace with the desired position in the Fibonacci sequence
print(f"The {n}th Fibonacci number is {fibonacci(n)}")
