class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next

        self.size += 1

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = self.head.prev

        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            res = self.tail.val
            self.tail = self.tail.prev

        self.size -= 1
        return res

    def popleft(self) -> int:
        if self.isEmpty():
            return -1        
        else:
            res = self.head.val
            self.head = self.head.next

        self.size -= 1
        return res
