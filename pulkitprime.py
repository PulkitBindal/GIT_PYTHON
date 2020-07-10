a=int(input("Enter the starting number"))
b=int(input("Enter the ending number"))
for i in range(a,b+1): 
      if i > 1: 
       for n in range(2,i): 
           if (i % n) == 0: 
               break
       else: 
           print(i)
#write a program in python to print prime numbers within the given range.
