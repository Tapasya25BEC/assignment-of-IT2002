# A9: Tail-recursive linear_sum converted to iterative

def linear_sum_tail(seq, i=0, acc=0):
    if i == len(seq):
        return acc
    return linear_sum_tail(seq, i + 1, acc + seq[i])

def linear_sum_iter(seq):
    acc = 0
    for x in seq:
        acc += x
    return acc

print(linear_sum_tail([1, 2, 3, 4]))
print(linear_sum_iter([1, 2, 3, 4]))
print(linear_sum_tail([]), linear_sum_iter([]))
