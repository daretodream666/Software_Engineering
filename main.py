def fib(n):
    fib1 = fib2 = 1
    with open("fib.txt", "w") as file:
        for _ in range(n):
            file.write(str(fib1) + "\n")
            yield fib1
            fib1, fib2 = fib2, fib1 + fib2


for i, val in enumerate(fib(200), start=1):
    if i == 200:
        print(val)
        break
