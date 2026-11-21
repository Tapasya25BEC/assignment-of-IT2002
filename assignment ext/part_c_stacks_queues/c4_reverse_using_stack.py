# C4: Reverse a sequence using a stack

def reverse_with_stack(seq):
    stack = []
    for x in seq:
        stack.append(x)
    result = []
    while stack:
        result.append(stack.pop())
    return result

print(reverse_with_stack([1, 2, 3, 4]))
print("".join(reverse_with_stack("hello")))
