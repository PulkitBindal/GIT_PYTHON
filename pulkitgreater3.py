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

