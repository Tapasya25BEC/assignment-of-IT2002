squares = [x ** 2 for x in range(1, 21)]
print("Squares of 1 to 20:", squares)

evens = [x for x in range(1, 51) if x % 2 == 0]
print("Even numbers from 1 to 50:", evens)

div_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print("Divisible by 3 and 5 (1 to 100):", div_by_3_and_5)
