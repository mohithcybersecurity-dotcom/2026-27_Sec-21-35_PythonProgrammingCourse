#python program to check whether a number is a prime number using for loop
number=int(input("Enter a number between 1 to 100 :"))

count = 0

for i in range(1, number + 1):  # values from 1 to number (use range)
    if number % i == 0:  # does number divide evenly by this value?
        count = count + 1  # increase count by 1 (or count += 1)

if count == 2:  # is count exactly 2?
    print(f"{number} is a prime number (divisor count = {count})")
else:
    print(f"{number} is not a prime number (divisor count = {count})")