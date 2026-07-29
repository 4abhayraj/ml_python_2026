import numpy as np

def find_first_repeating(arr):
    has_table = {}

    for num in arr:
        hash_table = {}

        for num in arr:
            hash_table[num] = hash_table.get(num, 0) +1
        for num in arr:
            if hash_table[num] > 1:
                return num
        return None
sample_array = [1,3,7,9,11,3,5]
result = find_first_repeating(sample_array)

print(f"Array: {sample_array}")
print(f"The first reeating element is: {result}")