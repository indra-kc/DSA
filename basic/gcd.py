def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 12
num2 = 18
gcd_value = gcd(num1, num2)
print(gcd_value)  # Output: 6
