#12,35,1,10,34,1
import array as arr
arr = arr.array("i",[12,35,1,10,34,1])
print(arr)
great=0
great_list=[]
for i in arr:
    for j in arr:
        if j==i:
            continue 
        elif i>great:
            great=i
        else:
            continue 
            
print(great)        
arr.remove(great)
print(arr)

s_great=0
for i in arr:
    for j in arr:
        if j==i:
            continue 
        elif j>i:
            s_great=j
        else:
            continue 
print("Second greatest no in array is :",s_great)                
