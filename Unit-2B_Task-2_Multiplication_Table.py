#python program to print the multiplication table
#Example for {for loop}
n=int(input("Enter the value:"))
for i in range(1,11):
    print(n,"x", i ,"=", n*i)

#Example for {while loop}
n=int(input("Enter the value:"))
i=0
while i<=10:
    print(n,"x", i ,"=", n*i)
    i=i+1 