class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.head = None

    def insert(self, key: int, val: int) -> None:
        print("INSERT", key, val)
        new_node = Node(key, val)
        if not self.head:
            self.head = new_node
            return
        
        def dfs(node):
            k = node.key
            if key < k:
                if not node.left:
                    node.left = new_node
                    return
                dfs(node.left)
            elif key > k:
                if not node.right:
                    node.right = new_node
                    return
                dfs(node.right)
            else:
                node.key = key
                node.val = val

        dfs(self.head)

    def get(self, key: int) -> int:
        print("GET", key)

        curr = self.head
        while curr:
            if curr.key < key:
                curr = curr.left
            elif curr.key > key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        print("GET_MIN")
        if not self.head:
            return -1

        node = self.findMin(self.head)
        return node.val


    def getMax(self) -> int:
        print("GET_MAX")
        if not self.head:
            return -1
            
        curr = self.head
        while curr.right:
            curr = curr.right
        return curr.val


    def remove(self, key: int) -> None:
        print("REMOVE", key)
        def dfs(node, curr_key):
            if not node:
                return None

            k = node.key
            # if curr_key smaller, go left
            if curr_key < k:
                node.left = dfs(node.left)

            # if curr_key bigger, go right
            elif curr_key > k:
                node.right = dfs(node.right) 
            
            # if curr_key match
            else:
                # 1 neighbor and no neighbor
                if node.left == None:
                    return node.right
                elif node.right == None:
                    return node.left

                # 2 neighbors
                else:
                    # find the minimum neighbor from the right nodes
                    min_node = node.right
                    while min_node and min_node.left:
                        min_node = min_node.left

                    # swap the position with current node
                    node.key = min_node.key
                    node.val = min_node.val
                    node.right = dfs(node.right, node.key)
            return node

        self.head = dfs(self.head, key)

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def removeHelper(self, node, key):
        if not node:
            return None

        if key > node.key:
            node.right = self.removeHelper(node.right, key)
        elif key < node.key:
            node.left = self.removeHelper(node.left, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self.findMin(node.right)
                node.key = min_node.key
                node.val = min_node.val
                node.right = self.removeHelper(node.right, min_node.key)


    def getInorderKeys(self) -> List[int]:
        print("GET_INORDER_KEYS")
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.key)
            dfs(node.right)

        dfs(self.head)

        return res
