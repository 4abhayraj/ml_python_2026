import array as arr

array1= arr.array("i",[10,20,30])

sum=0

for i in array1:
    print(i, end= ",")
    sum=i+sum
print("\nTotal sum is :", sum)