filename = "sample.txt"
old_word = "Python"
new_word = "Java"

with open(filename, "r") as file:
    content = file.read()

updated = content.replace(old_word, new_word)

with open(filename, "w") as file:
    file.write(updated)

print("Replaced", old_word, "with", new_word)