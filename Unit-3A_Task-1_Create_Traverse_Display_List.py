def print_details(**kwargs):  # **kwargs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Krishna", age=26, city="Guntur")  # Krishna, 26, Guntur