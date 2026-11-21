# A5/A6: Naive recursive Fibonacci and call counting

calls = 0

def fib(n):
    global calls
    calls += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for n in range(1, 11):
    calls = 0
    result = fib(n)
    print(f"fib({n}) = {result}, calls = {calls}")
calls = 0; fib(5); print("n=5 calls", calls)
