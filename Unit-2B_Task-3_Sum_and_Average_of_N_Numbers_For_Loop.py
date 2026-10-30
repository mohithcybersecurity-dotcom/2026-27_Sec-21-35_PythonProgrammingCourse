#Sum and average of N  numbers
n=int(input("Enter how many numbers:"))
sum=0
for input_index in range(n):
    entered_number=float(input("Enter a number:"))
    sum=sum+entered_number
average=sum/n
print(f"Sum={sum}")
print(f"Average={average}")

