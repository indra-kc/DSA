def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = sum(1 for char in s if char in vowels)
    return v, len(s) - v

# Example usage
text = "Hello World"  # Replace with any text you want to check
vowels, consonants = count_vowels_consonants(text)
print(f"Vowels: {vowels}, Consonants: {consonants}")
