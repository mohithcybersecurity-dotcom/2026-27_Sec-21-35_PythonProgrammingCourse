#python program to print continue statement 
n = int(input("Enter N (print 1 to N, skip even numbers): "))

for i in range(1, n + 1):  
    if i % 2 == 0:  
        print(f"Skipping even number {i} with continue (N is {n})")  
        continue
    print(f"for loop odd number = {i} (up to {n})")  