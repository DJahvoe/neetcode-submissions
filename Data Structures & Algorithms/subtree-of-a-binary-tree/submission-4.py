# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSametree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def isSametree(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
        if not first and not second:
            return True
        if not first or not second or first.val != second.val:
            return False
        
        return (self.isSametree(first.left, second.left) and self.isSametree(first.right, second.right))