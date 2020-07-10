def gcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

print("The H.C.F. is", gcd(num1, num2))
