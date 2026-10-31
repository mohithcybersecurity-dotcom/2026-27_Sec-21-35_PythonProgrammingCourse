#python program to find a number is a palindrome or not
num=int(input("Enter number:"))
org_num=num
reversed_num=0
while num>0:
    last_digit=num%10
    reversed_num=reversed_num*10+last_digit
    num=num//10
if reversed_num==org_num:
    print(f"{org_num} is a palindrome")
else:
    print(f"{org_num} is not a palindrome")