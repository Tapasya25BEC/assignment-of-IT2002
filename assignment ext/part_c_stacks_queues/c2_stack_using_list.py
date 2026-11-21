# C2: Stack ADT using a Python list

class Empty(Exception):
    pass

class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

s = Stack()
s.push(5); s.push(3)
print(s.top(), s.pop(), s.pop(), s.is_empty())
try:
    s.pop()
except Empty as e:
    print("Error:", e)
try:
    s.top()
except Empty as e:
    print("Error:", e)
print(len(s))
