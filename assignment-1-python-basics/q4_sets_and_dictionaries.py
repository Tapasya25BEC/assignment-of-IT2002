set_a = {1, 2, 3, 4, 5, 6}
set_b = {4, 5, 6, 7, 8, 9}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric difference:", set_a ^ set_b)

marks = {
    "Aman": 78,
    "Riya": 92,
    "Karan": 85,
    "Sneha": 67,
    "Rahul": 88,
}

print("\nStudent marks:")
for name, mark in marks.items():
    print(name, ":", mark)

topper = max(marks, key=marks.get)
print("\nHighest marks:", topper, "with", marks[topper])
