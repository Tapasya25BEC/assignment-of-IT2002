# C11: list vs collections.deque (removal from the front)

import timeit
from collections import deque

N = 100_000

def list_test():
    L = list(range(N))
    while L:
        L.pop(0)

def deque_test():
    D = deque(range(N))
    while D:
        D.popleft()

print("list.pop(0)   :", timeit.timeit(list_test, number=1))
print("deque.popleft :", timeit.timeit(deque_test, number=1))
