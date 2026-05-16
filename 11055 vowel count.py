"""sen= "loops are fun!a"
z=["a","e","i","o","u"]
tvow=0
tcon=0
for i in sen:
    if i==z:
        tvow+=1
elif i=="!"
        pass  
    else:
        tcon+=1    
print("total vowels are: ",tvow)
print("\n")
print("total consonents are: ",tcon) 

"""

sen="loops are fun!"
vow="aeiou"
v_count=0
c_count=0
for char in sen.lower():
    if char.isalpha():
        if char in vow:
            v_count+=1
        else:
            c_count+=1
print(f"Vowels: {v_count}")                
print(f"Consonents: {c_count}")