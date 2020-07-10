a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
n=int(input("Enter the number of terms needed..."))
print (a,b,end=" ")
for i in range(1,n+1):
	c=a+b
	a=b
	b=c
        break
print (c,end=" ")
n=n-1



