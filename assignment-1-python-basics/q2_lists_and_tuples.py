numbers = [12, 45, 7, 23, 56, 89, 34, 61, 18, 40]
print("Original list:", numbers)

numbers.append(100)
print("After adding 100:", numbers)

numbers.remove(7)
print("After removing 7:", numbers)

numbers.insert(2, 77)
print("After inserting 77 at position 2:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

numbers_tuple = tuple(numbers)
print("Tuple:", numbers_tuple)
print("Type:", type(numbers_tuple))
