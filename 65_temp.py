def remove_duplicate(nums):
    if not nums:
        return 0

    i=0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i]=nums[j]
    return i+1

arr = [1,1,2,2,3]       
k = remove_duplicate(arr)

print(f"Number of unique elements: {k}")
print(f"Modified array: {arr[:k]}")


        