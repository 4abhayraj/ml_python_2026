import array as arr

array1 = arr.array("i",[0,1,0,3,12])

print(array1)
for i in array1:
    print(i)
    if i==0:
        array1.remove(i)
        array1.append(i)
print(array1)        
