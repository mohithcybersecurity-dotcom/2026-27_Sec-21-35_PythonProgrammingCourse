s = input("Enter a string: ")

frequency = {}

for char in s:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

for key, value in frequency.items():
    print(key, ":", value)