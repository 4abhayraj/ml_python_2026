import numpy as np

def first_non_repeating(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    for num in arr:
        if counts[num] == 1:
            return num
    return None

arr = np.array([1, 2, 3, 6, 7, 7, 9, 11])
print(first_non_repeating(arr))