

#input three numbers.
x=int(input("Enter first number:"))
y=int(input("Enter second number :"))
z=int(input("Enter third number:"))
#procedure:compare each number .
if x>=y:
    if x>=z:
        largest=x
    else:
        largest=z
else:
    if y>=z:
        largest=y
    else:
        largest=z
#ouput:smallest number  will be printed.
print(f"largest={largest} (among:{x},{y}:{z})")