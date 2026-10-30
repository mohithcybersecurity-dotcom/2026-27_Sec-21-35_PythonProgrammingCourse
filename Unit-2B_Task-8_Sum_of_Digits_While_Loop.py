#python program to find sum of digits using while loop
number = int(input("Enter a number: "))
org_number = number 
digit_sum = 0

while number > 0:  
    digit = number % 10  
    digit_sum = digit_sum + digit  
    number = number // 10  
print(f"Sum of digits of {org_number} is {digit_sum}")