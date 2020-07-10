a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
n=int(input("Enter the number of terms needed..."))
print (a,b,end=" ")
while n>2 :
	c=a+b
	a=b
	b=c
	print (c,end=" ")
	n=n-1



