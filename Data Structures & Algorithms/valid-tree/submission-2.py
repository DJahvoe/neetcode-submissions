class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph_hash = {i: [] for i in range(n)}

        # create graph
        for e in edges:
            s, t = e
            # undirected graph
            graph_hash[s].append(t)
            graph_hash[t].append(s)

        # detect loop using DFS from root and its neighbor
        def dfs(val, visited, prev):
            if val in visited:
                return False
            # loop through neighbor
            for neighbor in graph_hash[val]:
                # skip self-loop
                if neighbor == prev:
                    continue
                visited.add(val)
                if not dfs(neighbor, visited, val):
                    return False
                visited.remove(val)
            return True
        
        # go through all roots
        for val, _ in graph_hash.items():
            if not dfs(val, set(), -1):
                return False
        return True