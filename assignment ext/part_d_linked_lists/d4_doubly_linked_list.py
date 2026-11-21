# D4: Doubly linked list (insert between, delete)

class DNode:
    def __init__(self, element, prev, next):
        self.element = element
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.header = DNode(None, None, None)
        self.trailer = DNode(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def insert_between(self, e, a, b):
        new = DNode(e, a, b)
        a.next = new
        b.prev = new
        self.size += 1
        return new

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        e = node.element
        node.prev = node.next = node.element = None
        return e

    def traverse(self):
        cur = self.header.next
        out = []
        while cur is not self.trailer:
            out.append(cur.element)
            cur = cur.next
        print(out)

D = DoublyLinkedList()
n1 = D.insert_between(10, D.header, D.trailer)
n2 = D.insert_between(30, n1, D.trailer)
D.insert_between(20, n1, n2)
D.traverse()
D.delete_node(n1)
D.traverse()
print(D.size)
