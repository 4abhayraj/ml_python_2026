"""
type code: i(2byte), I(2byte), u (unicode characcter, 2 byte), h(2byte), H(2byte), l(4byte), L(4byte), f(4byte), d(8 byte)
"""

import array

#first module then array we need to create then type code

val = array.array ('i', [1,2,3,4,5,6])

print(val)

print("\n")
#accessing array or iterating
for i  in range(0,6):            
    print(val[i], end=" ")

print("\n")
#enhanced for loop
for x in val:
    print(x,end=",")
