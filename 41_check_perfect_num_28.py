num=28

"""print(num//2)
num//=2
print(num//2)"""
sum=0


while True:
    num=num/2
    print(num)
    sum+=num
    if num<=0:
        break
print(sum)
if sum==28:
    print("28 is Perfect number")