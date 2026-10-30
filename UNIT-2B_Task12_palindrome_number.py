#python program to print a palindrome number 
number=int(input("Enter a number :"))

original_number = number
reversed_number = 0

while number > 0:  # reverse digits into reversed_number (see Task 10)
    digit = number % 10  # last digit with % 10
    reversed_number = reversed_number * 10 + digit  # build reverse: reversed_number * 10 + digit
    number = number // 10  # remove last digit with // 10

if reversed_number == original_number:  # compare reversed_number with original_number
    print(
        f"{original_number} is a palindrome "
        f"(reversed value is {reversed_number})"
    )
else:
    print(
        f"{original_number} is not a palindrome "
        f"(reversed value is {reversed_number})"
    )