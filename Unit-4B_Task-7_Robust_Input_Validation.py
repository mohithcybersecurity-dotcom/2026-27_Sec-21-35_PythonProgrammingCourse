class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter student marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")
except ValueError:
    print("Error: Please enter numbers only.")
except InvalidMarksError as e:
    print("Invalid Input:", e)
finally:
    print("Marks processing completed.")