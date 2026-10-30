#python program to print an inverted right angled triangle 
rows = int(input("Enter number of rows: "))
symbol=input("Enter a symbol:")
for i in range(rows, 0, -1):  
    for j in range(1, i + 1):  
        print(symbol, end=" ")  
    print()