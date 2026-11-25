from functools import reduce

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda a, b: a + b, numbers)

print("Squares:", squares)
print("Evens:", evens)
print("Sum:", total)