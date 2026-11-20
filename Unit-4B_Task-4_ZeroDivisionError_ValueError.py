try:
    num = int(input("Enter numerator: "))  # int or float
    den = int(input("Enter denominator: "))
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except ValueError:
    print("Please enter valid numbers.")
else:
    print("Quotient:",num/num)