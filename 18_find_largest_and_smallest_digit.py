def ls(num):
    max_digit=0
    smal_digit=9
    while num>0:
        current_no= num%10 #getS last digit
        if (current_no>max_digit):
            max_digit=current_no
        if (current_no<smal_digit):
            smal_digit=current_no
        
        num//=10
    print("Maximmum digit is: ",max_digit)
    print("smallest digit is: ",smal_digit) 
ls(75869)    




