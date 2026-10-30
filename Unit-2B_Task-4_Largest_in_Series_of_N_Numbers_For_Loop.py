#python program to find the largest number in the series
total_input_numbers=int(input("Enter any number:"))
largest = float(input("Enter a number: "))  # start with the first number

for i in range(total_input_numbers - 1):  # remaining numbers only (total_input_numbers - 1 times)
    current_number = float(input("Enter a number: "))  # read the next number
    if current_number > largest:  # is this number greater than largest?
        largest = current_number  # update largest

print(f"Largest among {total_input_numbers} numbers is {largest}")