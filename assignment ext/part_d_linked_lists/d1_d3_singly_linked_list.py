# D1/D3: Node and singly linked list

class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert_first(self, e):
        new = Node(e, self.head)
        self.head = new
        if self.size == 0:
            self.tail = new
        self.size += 1

    def insert_last(self, e):
        new = Node(e)
        if self.size == 0:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1

    def delete_first(self):
        if self.size == 0:
            raise IndexError("List is empty")
        e = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return e

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.element, end=" -> ")
            cur = cur.next
        print("None")

L = SinglyLinkedList()
L.insert_first(2); L.insert_first(1); L.insert_last(3)
L.traverse()
print(L.delete_first())
L.traverse()
L.delete_first(); L.delete_first()
print(L.is_empty(), L.head, L.tail)
L.insert_last(9); L.traverse()
try:
    L.delete_first(); L.delete_first()
except IndexError as e:
    print("Error:", e)
