#1,3,7,9,11,3,5

import numpy as np

arr= np.array([1,3,7,9,11,3,5])

count=0

for i in arr:
    count+=1

print(f"count total numer of element is: {count}")

sum=0
for i in arr:
    sum+=i
print(f"sum of arr is: {sum}") 

print(f"average of element in array is: {sum/count}")