try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    print("Error: please enter valid numbers")
else:
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)

    if b == 0:
        print("Quotient: not defined (division by zero)")
        print("Remainder: not defined (division by zero)")
    else:
        print("Quotient:", a / b)
        print("Remainder:", a % b)
