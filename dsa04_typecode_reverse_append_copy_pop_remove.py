from array import *
val = array('i',[1,2,3,4,5,6,7,8,9])

for i in range(0, len(val)):
    print(val[i] , end= " ")

print("\n")

for x in val:
    print(x, end=", ")

print("\n")

print("typecode of val is: ",val.typecode)


#reverse the array
val.reverse()

for i in range(0, len(val)):
    print(val[i], end=" ")

print("\n")
# insert array index
#(index, value)
val.insert(1,50)

for i in range (0, len(val)):
    print(val[i],end=",")

print("\n")
#append 
val.append(100)

for i in range(0,len(val)):
    print(val[i],end=",")

print("\n")
# overwrite array  using index
val[2] = 200
for i in range(0, len(val)):
    print(val[i],end=" ")


print("\n")
#copy array
#typecode element mention 
copyArray = array(val.typecode ,(x for x in val))

for i in range(0,len(val)):
    print(copyArray[i] , end=" ")

print("\n delete array \n")

#delete array using pop 

copyArray.pop(3) #3 is index, if no index is given it will delete last element

for i in range(0,len(copyArray)):
    print(copyArray[i], end=",")

print("\n")
#remove
copyArray.remove(3) #3 is an element, and it will be removed *3 is not index

for i in range(0, len(copyArray)):
    print(copyArray[i], end=" ")
