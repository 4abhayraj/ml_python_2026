n_terms=10
#0,1,1,2,3,5,8,13,21


my_list=[None]*10
print(my_list)
print(len(my_list))

my_list[0], my_list[1]=0,1
for i in range(2,len(my_list)):
    if i==1:
        my_list[i]=1
        continue
    my_list[i]=my_list[i-2]+my_list[i-1]

print(my_list)




