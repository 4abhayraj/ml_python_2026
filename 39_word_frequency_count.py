text= "apple banana apple orange banana apple"

list1=text.split()

temp=[]
count=0
print(list1)
for i in range (len(list1)):
    if list1[i] not in temp:
        temp.append(list1[i])
    else :
        count+=1

print(temp)
print(count)

