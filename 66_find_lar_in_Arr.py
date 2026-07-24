# array= [1,3,7,9,11,3,5]
import numpy as np

arr =np.array([1,3,7,9,11,3,5])

largest=0

for i in arr:
    if i>largest:
        largest=i
    else:
        continue    
print(f"largest element in an array is: {largest}")
