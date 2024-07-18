def fibonacci(n):
    fib_1, fib_2 = 0, 1
    for i in range(n):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2


fib_gen = list(fibonacci(10))


print(fib_gen)
