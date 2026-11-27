counter = 0

def increment():
    global counter
    counter = counter + 1
    print("Inside function, counter =", counter)

print("Before:", counter)
increment()
print("After:", counter)
