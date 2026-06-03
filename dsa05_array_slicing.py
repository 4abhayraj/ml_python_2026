from array import *
#      index =>   0               8
val = array ('i',[1,2,3,4,5,6,7,8,9])
#      index =>  -9               -1
#[start index : end index : step]
abc = val[2:5]
abc = val[2:-3]
abc = val[::-1]
for i in range(0,len(abc)):
    print(abc[i] , end=' ')

