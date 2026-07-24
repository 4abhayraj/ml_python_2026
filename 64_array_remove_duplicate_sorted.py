"""import array as ar
def remove_duplicates(nums):
    if not nums:
        return 0
        
    # 'i' tracks the index of the last unique element found
    i = 0
    
    # 'j' iterates through the array
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            
    # The number of unique elements is i + 1
    # To see the modified array up to the unique elements: nums[:i+1]
    return i + 1

# Test the function
arr = ar.array("i",[1, 1, 2, 2, 3,7,7,8,9,9,9])
k = remove_duplicates(arr)

print(f"Number of unique elements: {k}")
print(f"Modified array: {arr[:k]}")
"""

##################################################

import array as arr

def remove_duplicate(nums):
    if not nums:
        return 0
    i=0
    for j  in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
ar = arr.array("i",[1,1,1,2,2,3])
k = remove_duplicate(ar)

print(f"no. of unnique elements: {k}")
print(f"Modified array: {ar[:k]}")