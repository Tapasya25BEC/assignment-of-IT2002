# B6: Two-dimensional dataset using nested lists

marks = [
    [80, 75, 90],
    [60, 85, 70],
    [95, 88, 92],
]

print("Row 1:", marks[1])
print("Column 0:", [row[0] for row in marks])
print("Element [2][1]:", marks[2][1])

for r in marks:
    print(sum(r) / len(r))
