def two_sum(nums, target):
    # Dictionary to store the number and its index
    num_map = {}
    
    for i, num in enumerate(nums):
        # Calculate what number we need to hit the target
        complement = target - num
        
        # If the complement is in our map, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
            
        # Otherwise, add the current number and its index to the map
        num_map[num] = i
        
    return [] # Return empty if no pair is found

# Test the function (assuming a target of 9)
arr = [2, 7, 11, 15]
target_val = 9
indices = two_sum(arr, target_val)

print(f"Indices for target {target_val}: {indices}")