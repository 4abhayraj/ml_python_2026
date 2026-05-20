binary_str="1101"
num=0
for bit in (binary_str):
    num =  num * 2 + int(bit)
print(num)