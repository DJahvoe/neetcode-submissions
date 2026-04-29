"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldStore = {None: None}

        cur = head
        while cur:
            newNode = Node(cur.val)
            oldStore[cur] = newNode
            cur = cur.next
        
        cur = head
        while cur:
            newNode = oldStore[cur]
            newNode.next = oldStore[cur.next]
            newNode.random = oldStore[cur.random]
            cur = cur.next
        
        return oldStore[head]
