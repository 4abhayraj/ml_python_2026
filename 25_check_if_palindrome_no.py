#check if a number is palindrome or not

num=int(input("Enter a number: "))

text=str(num)
print(len(text))
my_bool=None
for i in range (0,len(text)):
    if (text[i]==text[-i-1]):
        my_bool=True
    else:
        my_bool=False
if my_bool==True:
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")