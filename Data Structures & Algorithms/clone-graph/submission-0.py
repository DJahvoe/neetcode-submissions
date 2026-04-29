"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        map_old_to_new = {}
        map_old_to_new[node] = Node(node.val)
        q = deque([node])

        while q:
            current = q.popleft()
            for n in current.neighbors:
                if n not in map_old_to_new:
                    map_old_to_new[n] = Node(n.val)
                    q.append(n)
                map_old_to_new[current].neighbors.append(map_old_to_new[n])
        
        return map_old_to_new[node]