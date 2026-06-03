"""
import numpy as np
np.array
"""
#in numpy no need to write typecode in numpy array
"""
immport numpy 
numpy.array
"""

'''
from numpy import *
array()
'''

from numpy import *
val = array([1,2,4])

for x in val:
    print(x, end=" ")

print("\n")

val2 = array([1,2,4.5,"a"]) 
#in numpy array we can store hetrogeneous types of elements like int float
#if we add character with int then it will be hetrogeneous array, otherwise homogeneous array


for x in val2:
    print(x, end=" ")


print("\n")
val3 = array([1,2,4], float)  #datatype mentioned here

for x in val3:
    print(x, end=",")