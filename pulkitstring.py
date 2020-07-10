string=[20,30,40,50,60]
print(string)
print(string[2:4])
print(string[:4])
print(string[::-1])
a,b=input("Enter the starting and ending indexes..:").split()
a,b=int(a),int(b)
print(string[a-1:b])
