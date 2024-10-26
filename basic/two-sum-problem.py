def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# Example usage
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1] (2 + 7 = 9)
print(two_sum([3, 2, 4], 6))       # Output: [1, 2] (2 + 4 = 6)
print(two_sum([1, 5, 3, 8], 8))    # Output: [0, 2] (5 + 3 = 8)
