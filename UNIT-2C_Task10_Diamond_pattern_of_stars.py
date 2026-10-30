#python program to print a diamond pattern of stars
rows = int(input("Enter number of rows (half diamond): "))

for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()