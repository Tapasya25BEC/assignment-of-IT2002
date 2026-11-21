# A2: Factorial, sum of first n natural numbers, x^n

def factorial(n):
    if n == 0:   # base case
        return 1
    return n * factorial(n - 1)

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(factorial(5))
print(sum_n(10))
print(power(2, 10))
