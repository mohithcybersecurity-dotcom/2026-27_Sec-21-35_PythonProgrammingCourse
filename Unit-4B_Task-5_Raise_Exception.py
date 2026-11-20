try:
    age = int(input("Enter age:"))
    if age < 0:  # e.g. 0
        raise ValueError("Age cannot be negative.")
    print("Valid age:", age)
except ValueError as err:
    print("Error:", err)