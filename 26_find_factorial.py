#find factorial of anumber
num=int(input("Enter anumber: "))
sum=1
for i in range(num,0,-1):
    sum=sum*i

print(f"factorial of {num} is: {sum}")