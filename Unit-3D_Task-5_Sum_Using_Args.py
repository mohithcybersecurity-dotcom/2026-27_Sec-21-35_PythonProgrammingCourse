def sum_values(*args):
    total=0
    for value in args:
        total=total+value
    return total
total=sum_values(1,3,4)
print(total)