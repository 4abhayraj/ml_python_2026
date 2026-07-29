#1,3,7,9,11,3,5
import numpy as np
arr=np.array([1,3,7,9,11,3,5])
print(arr)
even=0
odd=0
for i in arr:
     if i%2==0:
          even+=1

     elif i%2!=0:
          odd+=1
     else:
          continue
print(f"number of even in array is: {even}")
print(f"number of odd in array is: {odd}")     