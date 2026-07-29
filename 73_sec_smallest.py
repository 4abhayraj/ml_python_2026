#1,3,7,9,11,3,5

import numpy as np

arr=np.array([1,3,7,9,11,3,5])

f_smallest=999
target_count=0
count=0

for i in arr:
    if i<f_smallest:
        f_smallest=i
        target_count=count
    count+=1

new_arr=np.delete(arr,target_count)

sec_small=999
for i in new_arr:
    if i<sec_small:
        sec_small=i
    else:
        continue

print(f"the Second largest element in the array is: {sec_small}")