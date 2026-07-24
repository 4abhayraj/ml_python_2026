#15,42,7,23

import array as arr
array2 = arr.array('i',[15,42,7,23])

print(array2)

great=0
lowest=999
for i in array2:
    print(i,"\n\n")
    for j in array2:
        
        if j == i:
            continue 
        elif j>great:
            great = j
        elif j<lowest:
            lowest=j         
        print(j,end= ",")
    print("\n\n")   
print("greatest no. : ", great) 
print("lowest no. : ",lowest)    