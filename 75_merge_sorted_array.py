import numpy as np

sorted_arr_1=np.array([1,2,3,4])

sorted_arr_2=np.array([5,6,7,8])

merged_arr=np.concatenate((sorted_arr_1,sorted_arr_2))

print(f"Merged array is: {merged_arr}")