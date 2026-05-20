#find factorial of a number
def factorial(num):
    sum=1
    for i in range(num,0,-1):
        sum=sum*i

    print(f"factorial of {num} is: {sum}")
factorial(5)
factorial(10)