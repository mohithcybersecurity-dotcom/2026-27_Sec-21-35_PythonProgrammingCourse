dict_data = {x: x * x for x in range(1, 6)}
print("Squares dict:", dict_data)

# optional: only even keys
dict_even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print("Even squares:", dict_even_squares)