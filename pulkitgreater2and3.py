def fun1():
    
    num1=int(input("ENTER FIRST NUMBER"))
    num2=int(input("ENTER SECOND NUMBER"))
    num3=int(input("ENTER THIRD NUMBER"))
    if (num1>num2) and (num1>num3) :
     large=num1
    elif (num2>num1) and (num2>num3) :
     large=num2
    elif num1==num2==num3 :
     print("All numbers are same")
    else :
     large=num3
    print("The largest number is:",large)
def fun2():
    num1=int(input("ENTER FIRST NUMBER"))
    num2=int(input("ENTER SECOND NUMBER"))
    if num1>num2 :
     print("The largest number is",num1)
    else :
     print("The largest number is:",num2)

a=int(input("How many numbers you want to insert...:"))
if a==1: 
    print ("Please Enter either 2 or 3....")
elif a==2:
   fun2()
elif a==3:
   fun1()
else :
    print ("Please Enter a valid number either 2 or 3...")
