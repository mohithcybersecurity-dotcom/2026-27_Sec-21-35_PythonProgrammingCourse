#python program to find the factorial of a number 
number=int(input("number"))
factorial = 1  # start with 1

for i in range(1, number + 1):  # values from 1 to number (use range)
    factorial = factorial * i  # multiply factorial by the current value

print(f"Factorial of {number} is {factorial}")