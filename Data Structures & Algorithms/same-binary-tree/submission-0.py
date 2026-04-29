# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # append, popleft
        p_bfs = deque([p])
        q_bfs = deque([q])
        is_same_flag = True

        while len(p_bfs) > 0 and len(q_bfs) > 0:
            top_p = p_bfs.popleft()
            top_q = q_bfs.popleft()
            if top_p == None and top_q == None:
                continue

            if (top_p == None and top_q != None) or (top_p != None and top_q == None):
                return False
            if top_p.val != top_q.val:
                return False
            p_bfs.append(top_p.left)
            p_bfs.append(top_p.right)
            q_bfs.append(top_q.left)
            q_bfs.append(top_q.right)
        return True