#python program to check whether a number is prime number or not 

number = int(input("Enter a number between 1 and 100: "))

if number < 1 or number > 100:  # number is outside 1 to 100?
    print(f"{number} is not between 1 and 100")
elif number == 1:  # 1 is not prime
    print(f"{number} is not a prime number")
elif number in (2, 3, 5, 7):  # number is 2, 3, 5, or 7?
    print(f"{number} is a prime number")
elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:  # divisible by 2, 3, 5, or 7?
    print(f"{number} is not a prime number")
else:
    print(f"{number} is a prime number")