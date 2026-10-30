#check whether a number is positive or negative or zero
#input a number 
number=int(input("Enter a number :"))
#process check the number is positive or negative or zero 
if number>0:
#output:positive or negative or zero
    print(f"{number} is a positive number")
elif number<0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is equal to zero ")