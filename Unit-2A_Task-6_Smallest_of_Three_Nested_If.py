#to find smallest of three numbers.
#input three numbers.
x=int(input("Enter first number:"))
y=int(input("Enter second number :"))
z=int(input("Enter third number:"))
#procedure:compare each number .
if x<=y:
    if x<=z:
        smallest=x
    else:
        smallest=z
else:
    if y<=z:
        smallest=y
    else:
        smallest=z
#ouput:smallest number  will be printed.
print(f"smallest={smallest} (among:{x},{y}:{z})")