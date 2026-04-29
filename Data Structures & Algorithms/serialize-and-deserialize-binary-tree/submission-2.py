# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import json
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree_arr = []
        tree_deque = deque([root])
        while len(tree_deque) > 0:
            curr = tree_deque.popleft()
            if not curr:
                tree_arr.append(None)    
                continue
            tree_arr.append(curr.val)
            tree_deque.append(curr.left)
            tree_deque.append(curr.right)
        print(tree_arr)
        return json.dumps(tree_arr)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree_arr = json.loads(data)
        if tree_arr[0] == None:
            return None
        
        root = TreeNode(tree_arr[0])
        tree_deque = deque([root])
        k = 1
        while tree_deque:
            curr = tree_deque.popleft()
            if tree_arr[k] != None:
                curr.left = TreeNode(tree_arr[k])
                tree_deque.append(curr.left)
            k += 1
            if tree_arr[k] != None:
                curr.right = TreeNode(tree_arr[k])
                tree_deque.append(curr.right)
            k += 1
        return root
            


