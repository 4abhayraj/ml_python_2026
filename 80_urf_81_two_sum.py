import numpy as np

def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

arr = np.array([1, 2, 3, 6, 7, 7, 9, 11])
target = 9
print(two_sum(arr, target))