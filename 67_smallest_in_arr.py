import numpy as np
arr= np.array ([1,3,7,9,11,3,5])
smallest=999


for i in arr:
    if i<smallest:
        smallest=i
    else:
        continue
print(F"Smallest no. in array is: {smallest}")