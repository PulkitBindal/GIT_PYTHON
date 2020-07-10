num=int(input("Enter the number of terms needed..:"))
a=0
b=1
print(a)
print(b)
while(num>2):
	c=a+b
	print(c)
	a=b
	b=c
	num=num-1

