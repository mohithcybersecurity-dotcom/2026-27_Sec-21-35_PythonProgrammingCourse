#python program to count digits using whiile loop
num=int(input("Enter number:" ))
org_num=num
count=0
if num==0:
    count=1
else:
    while count<=num:
        count=count+1
        num=num//10
print(f"Number of digits in {org_num} is {count}")