class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        tempPrev = self.tail.prev
        tempNext = self.tail
        node.prev, node.next = tempPrev, tempNext
        tempPrev.next = tempNext.prev = node

    def remove(self, node):
        tempPrev = node.prev
        tempNext = node.next
        tempPrev.next = tempNext
        tempNext.prev = tempPrev
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dll = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.dll.remove(self.cache[key])
            self.dll.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.dll.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.dll.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            left_most = self.dll.head.next
            self.dll.remove(left_most)
            del self.cache[left_most.key]
