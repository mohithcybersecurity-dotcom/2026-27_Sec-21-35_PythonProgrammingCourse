source = "sample.txt"
destination = "copy.txt"
with open(source, "r") as src:
    content = src.read()
with open(destination, "w") as dest:
    dest.write(content)
print("Copied from", source, "to", destination)