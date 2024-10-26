import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Example usage
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]  # Example list
    k = 2                       # We want to find the 2nd largest element
    result = find_kth_largest(nums, k)
    print(f"The {k}th largest element is: {result}")
