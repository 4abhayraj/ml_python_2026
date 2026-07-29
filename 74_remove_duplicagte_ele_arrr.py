#1,3,7,9,11,3,5

import numpy as np

arr=np.array([1,3,7,9,11,3,5])
pointer=0
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if i==j:
            continue
        elif arr[i]==arr[j]:
            
            new_arr=np.delete(arr,i)
print(f"old array: {arr}")
print(f"modified array: {new_arr}")