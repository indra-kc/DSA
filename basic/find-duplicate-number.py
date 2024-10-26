def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow

# Example usage
if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]  # Duplicate number is 2
    duplicate_number = find_duplicate(nums)
    print(f"The duplicate number is: {duplicate_number}")
