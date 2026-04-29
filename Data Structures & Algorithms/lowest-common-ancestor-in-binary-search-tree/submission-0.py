# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_val, q_val = p.val, q.val
        if p_val > q_val:
            p_val, q_val = q_val, p_val

        # find the correct subtree root
        while root:
            if p_val == root.val or q_val == root.val:
                break
            if p_val < root.val < q_val:
                break
            elif root.val < p_val and root.val < q_val:
                print("RIGHT")
                root = root.right
            elif root.val > p_val and root.val > q_val:
                print("LEFT")
                root = root.left
        
        return root
