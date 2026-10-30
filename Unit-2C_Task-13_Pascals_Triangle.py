rows = int(input("Enter number of rows: "))

for row_loop_var in range(1, rows + 1):
    for column_loop_var_spaces in range(1, rows - row_loop_var + 1):
        print(" ", end="")
    value = 1
    for column_loop_var in range(1, row_loop_var + 1):
        print(value, end=" ")
        value = value * (row_loop_var - column_loop_var) // column_loop_var
    print()
    