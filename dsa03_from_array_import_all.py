from array import *

val = array ('i',[1,2,3,4,5,6,7,8,9])

val2 = array ('d',[1,2,3,4,5,9.5])

val3 = array ('u', ['a','b','c','d'])

for i in range(0,len(val2)):
    print(val2[i], end=" ")

print("\n")

for x in val2:
    print(x,end=",")
print('\n')
for x in val3:
    print(x,end=",")

# to know array type code
print('\n')
print("type code of val is:",val.typecode)