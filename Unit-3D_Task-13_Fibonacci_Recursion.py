def fib(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fib(k - 1) + fib(k - 2)

n = 7
for i in range(n):
    print(fib(i), end=" ")