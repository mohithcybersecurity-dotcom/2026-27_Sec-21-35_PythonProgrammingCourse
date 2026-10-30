#python program to print pass statement 
n = int(input("Enter N (use pass for multiples of 3): "))
for i in range(1, n + 1):  
    if i % 3 == 0:  
        pass  
        print(f"Used pass for multiple of 3: {i} (N is {n})")  
    else:
        print(f"for loop number = {i} (up to {n})")  