def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Factorial is not defined for negative numbers")
    else:
        print("Factorial of", num, "is", factorial(num))

    terms = int(input("Enter number of terms for Fibonacci: "))
    print("Fibonacci series:", fibonacci(terms))

    check = int(input("Enter a number to check prime: "))
    if is_prime(check):
        print(check, "is a prime number")
    else:
        print(check, "is not a prime number")
except ValueError:
    print("Error: please enter valid whole numbers")
