filename = "output.txt"
text = "Learning file handling in Python."
with open(filename, "w") as file:
    file.write(text)
print("Data written to", filename)