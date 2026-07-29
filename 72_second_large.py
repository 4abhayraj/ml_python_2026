#1,3,7,9,11,3,5
import numpy as np
arr=np.array([1,3,7,9,11,3,5])
f_largest=0
count=0
t_count=0
for i in arr:   
    if i>f_largest:
        f_largest=i
        t_count=count
    count+=1
new_arr=np.delete(arr,t_count)
s_largest=0
for i in new_arr:
    if i>s_largest:
        s_largest=i
    else:
        continue
print(f"Second largest element in array is: {s_largest}")