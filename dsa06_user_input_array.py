from array import *

arr = array( 'i' ,[])

n=int(input("Enter a numbber : "))

for i in range(0,n):
    arr.append(int(input("Enter next input : ")))

#enhanced for loop
for x in arr:
    print(x, end=" ")