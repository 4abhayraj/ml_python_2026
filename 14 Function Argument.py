#Types of function Arguments


#Default Argument: it is a parameter that assumes a default value if a value is not provided in function call for that argument
#(first empty parameter whill be alloted default value else syntax error)
'''
def myfunc(x,y=50):
    print("x: ",x)
    print("y: ",y)

myfunc(10)
'''
#def newfunc(x=60,y,z=20): 
def newfunc(y,x=60,z=20):
    print("x: ",x)
    print("y: ",y)
    print("z: ",z)
newfunc(30)


print("\n\n")
#keyword argument
'''
def student(fname,lname):
    print(fname,lname)

student(fname="Abhay", lname="Raj")
student(lname="Raj", fname="Abhay")

'''
#keyword argument
def sir(fname,lname):
    print(fname,lname)
sir(fname="Sachin",lname="Yadav")
sir(lname="Yadav",fname="Sachin")    


print("\n\n\n")


#Positional Arguments
def nameAge(name,age):
    print("hi, i am ",name)
    print("my age is ",age)
print("Case-1")    
nameAge("Abhay",21)    
print("Case-2")
nameAge(21,"Abhay")
print("\n\n\n")

#Arbitrary Arguments
def afunc(*args,**kargs):
    print("non-keywords Arguments (*args):")
    for arg in args:
        print(arg)
    print("\n Keyword argumnets (**kargs):")
    for key,value in kargs.items():
        print(f"{key}:{value}")
afunc('Hello','Abhay',first="Sachin", mid="yadav", last="sir CU")            