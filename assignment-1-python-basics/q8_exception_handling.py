try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: cannot divide by zero")
except ValueError:
    print("Error: please enter valid numbers")
finally:
    print("Program finished")
