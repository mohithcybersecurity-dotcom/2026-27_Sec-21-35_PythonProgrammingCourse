#python program to find the armstrong number
num=int(input("Enter a 3-digit number:"))
org_num=num
total=0
while num>0:
    digit=num%10
    total=total+digit**3
    num=num//10
if total == org_num:
    print(f"{org_num} is an Armstrong number")
else:
    print(f"{org_num} is not an Armstrong number")