try:
    a=int(input("Enter numerator:"))
    b=int(input("Enter denominator:"))
    result=a/b
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter valid numbers.")
else:
    print("Result:",result )  # runs only if try succeeded
finally:
    print("program finished")