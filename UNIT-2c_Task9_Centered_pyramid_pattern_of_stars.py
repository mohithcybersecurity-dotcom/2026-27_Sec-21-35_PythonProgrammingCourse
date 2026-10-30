#python program to print the centered pyramid of stars 
rows = 3  

for i in range(1, rows + 1): 
    for j in range(1, rows - i + 1):  
        print(" ", end=" ")
    for k in range(1, 2 * i):  
        print("*", end=" ")  
    print()