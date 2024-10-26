def are_anagrams(s1, s2):
    print("Sorted s1:", sorted(s1))
    print("Sorted s2:", sorted(s2))
    return sorted(s1) == sorted(s2)

# Example usage
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("rat", "car"))        # False
