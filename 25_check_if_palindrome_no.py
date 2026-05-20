#check if a number is palindrome or not
def palindrome(num):
    text=str(num)
#    print(len(text))
    my_bool=None
    for i in range (0,len(text)):
        if (text[i]==text[-i-1]):
            my_bool=True
        else:
            my_bool=False
    if my_bool==True:
        print(f"The {num} is palindrome")
    else:
        print(f"The {num} is not palindrome")
palindrome(121)
palindrome(343)