# A4: Check if a sequence is sorted (non-decreasing)

def is_sorted(seq, i=0):
    if i >= len(seq) - 1:   # base case
        return True
    if seq[i] > seq[i + 1]:
        return False
    return is_sorted(seq, i + 1)

print(is_sorted([1, 2, 2, 5]))
print(is_sorted([3, 1, 2]))
print(is_sorted([]), is_sorted([7]))
