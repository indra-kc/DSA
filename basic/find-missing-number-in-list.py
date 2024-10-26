def find_missing(nums):
    n = len(nums) + 1
    return n * (n - 1) // 2 - sum(nums)

# Example usage
if __name__ == "__main__":
    nums = [0, 1, 2, 3, 5]  # Missing number is 4
    missing_number = find_missing(nums)
    print(f"The missing number is: {missing_number}")
