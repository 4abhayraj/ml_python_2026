n=153
num=153
number=153
count=0

#getting no. of digits
while True:

    count+=1
    n=n//10
    if n<=0:
        break
print("Numbers of digit: ",count)

sum=0
while True:
    p=num%10
    num//=10
    c=p**count
    sum+=c
    if num<=0:
        break

if sum==number:
    print("The given number is armstrong")
