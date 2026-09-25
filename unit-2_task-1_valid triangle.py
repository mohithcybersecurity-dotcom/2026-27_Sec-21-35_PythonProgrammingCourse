#To find whether trinagle is valid or not .
#Input three numbers.
angle1_in_degrees=int(input("Enter first number:"))
angle2_in_degrees=int(input("Enter second number:"))
angle3_in_degrees=int(input("Enter third number:"))
#process check whether three angles are equal to 180degrees and greater than zero.
if (
    angle1_in_degrees > 0
    and angle2_in_degrees > 0
    and angle3_in_degrees > 0
    and angle1_in_degrees + angle2_in_degrees + angle3_in_degrees == 180):
#output the triangle is valid or not 
    print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is valid")
else:
    print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is not valid")
