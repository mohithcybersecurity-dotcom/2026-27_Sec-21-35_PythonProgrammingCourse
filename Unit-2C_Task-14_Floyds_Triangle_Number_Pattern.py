rows = int(input("Enter number of rows: "))
rows = int(input("Enter number of rows: "))
num = 1  # start from 1

for row_loop_var in range(1, rows + 1):  # row_loop_var; range(1, rows + 1)
    for column_loop_var in range(1, row_loop_var + 1):  # column_loop_var; range(1, row_loop_var + 1)
        print(num, end=" ")  # print current number
        num = num + 1  # increase num by 1
    print()