#Write a python program to print numbers from 1 to N
#exapmle for {for loop}
limit=int(input("Enter the value of N:"))
for current_number in range(1,limit+1):
    print(current_number)

#example for {while loop}
limit=int(input("Enter the value of N:"))
count=0
while count<=limit:
    print(count)
    count=count+1