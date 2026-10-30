#python program to display a break statement 
n = int(input("Enter N (print until N, stop early at 5): "))

for i in range(1, n + 1):  
    if i == 5:  
        print(f"Breaking for loop at number {i} (N was {n})")  
        break
    print(f"for loop number = {i} (up to {n})")  