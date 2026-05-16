def armstrong(given_num):
    count=0
    num=given_num
    num1=given_num
#counting digits

    while num>0:
        num//=10
        count+=1
    print("total number of digits in given number: ",count)

#checking armstrong no.
    sum=0
    for i in range (count):
        x=num1%10
        print(x)
        a=x**count
        num1//=10
        print(f"{"cube" if count==3 else "power four"} for {i} digit",a)
        sum+=a
    print(sum)
    print("\n\n")
    if sum==given_num:
        print(f"{given_num} is armstrong number")
    else:
        print(f"{given_num} is not armstong number")    
armstrong(153)    
armstrong(9999)
armstrong(given_num=9474)