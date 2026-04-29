# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        node_counter = 0

        def findGoodNodes(node, biggest):
            nonlocal node_counter
            if not node:
                return
            
            if node.val >= biggest:
                node_counter += 1
            
            findGoodNodes(node.left, max(node.val, biggest))
            findGoodNodes(node.right, max(node.val, biggest))
        
        findGoodNodes(root, -101)
        return node_counter
        