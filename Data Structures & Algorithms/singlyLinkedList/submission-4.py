class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # dummy node for easier operation
        self.head = Node(-1)
        self.tail = self.head
        
    
    def get(self, index: int) -> int:
        cur = self.head.next
        # head is Null
        if not cur:
            return -1

        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        # if index out of bound (Null)
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        next_node = self.head.next

        self.head.next = new_node
        new_node.next = next_node

        # If list was empty before insertion
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while i < index and cur:
            i += 1
            cur = cur.next

        # Remove node after curr
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        cur = self.head.next
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr
        
