# C10: Deque using circular-array indexing

class Empty(Exception):
    pass

class ArrayDeque:
    def __init__(self, capacity=8):
        self._data = [None] * capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        idx = (self._front + self._size) % len(self._data)
        self._data[idx] = e
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return ans

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        ans = self._data[back]
        self._data[back] = None
        self._size -= 1
        return ans

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

d = ArrayDeque(4)
d.add_last(1); d.add_last(2); d.add_first(0); d.add_first(-1); d.add_last(3)
print(d.delete_first(), d.delete_last(), d.delete_first(), len(d))
try:
    ArrayDeque().delete_last()
except Empty as e:
    print("Error:", e)
