# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        multiplier = 1
        bfs_list = deque([[root, 0]])
        output = []

        temp = []
        temp_level = 0
        while len(bfs_list) > 0:
            current_node, level = bfs_list.popleft()
            if current_node == None:
                continue
            if temp_level != level:
                output.append(temp)
                temp = []
                temp_level += 1
            
            temp.append(current_node.val)
            bfs_list.append([current_node.left, level + 1])
            bfs_list.append([current_node.right, level + 1])
        if len(temp) > 0:
            output.append(temp)
        return output
                

