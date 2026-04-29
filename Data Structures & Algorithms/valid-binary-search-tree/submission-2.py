# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isNodeValid(node, minimal, maximal):
            # Null node
            if not node:
                return True
            
            return (isNodeValid(node.left, minimal, node.val) and
                    isNodeValid(node.right, node.val, maximal) and
                    minimal < node.val < maximal)

        
        return isNodeValid(root, float("-inf"), float("inf"))
        
        

        
        

        