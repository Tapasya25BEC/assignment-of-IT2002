# A3: Recursive in-place reversal using start and stop indices

def reverse(seq, start, stop):
    if start >= stop:   # base case
        return
    seq[start], seq[stop] = seq[stop], seq[start]
    reverse(seq, start + 1, stop - 1)

data = [1, 2, 3, 4, 5, 6]
reverse(data, 0, len(data) - 1)
print(data)
