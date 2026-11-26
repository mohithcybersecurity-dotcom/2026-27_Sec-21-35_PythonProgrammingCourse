dict_data = {"maths": 80, "science": 75, "english": 90}

print("Keys:")
for key in dict_data:
    print(key)

print("Values:")
for value in dict_data.values():
    print(value)

print("Items:")
for key, value in dict_data.items():
    print(key, "→", value)