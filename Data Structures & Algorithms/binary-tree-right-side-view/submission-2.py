# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_side_result = {}

        def findMostRight(node, height):
            if not node:
                return
            
            findMostRight(node.right, height + 1)
            if height not in right_side_result:
                right_side_result[height] = node.val
            findMostRight(node.left, height + 1)
        
        right_side_result[0] = root.val
        findMostRight(root, 0)

        result = []
        for i in range(len(right_side_result)):
            result.append(right_side_result[i])

        return result