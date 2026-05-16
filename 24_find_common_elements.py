list_a=[1,2,3,4,5]
list_b=[4,5,6,7,8]
common_list=[]

for i in range(0,len(list_a)):
    for j in range(0,len(list_b)):
        if list_a[i]==list_b[j]:
            common_list.append(list_a[i])
print(common_list)            