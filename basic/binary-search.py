def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]  # Sorted array
    target = 4                 # Target number to search for
    result = binary_search(arr, target)
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found.")
