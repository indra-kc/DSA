rotate_by_k = lambda arr, k: [arr[-k+i] for i in range(len(arr))]

arr = [1, 2, 3, 4, 5]
print(rotate_by_k(arr, 1))
