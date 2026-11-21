# B3: Dynamic array (what happens when it is full)

import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(1)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

d = DynamicArray()
for i in range(5):
    d.append(i)
print(len(d), d[4])
try:
    d[10]
except IndexError as e:
    print("Error:", e)
