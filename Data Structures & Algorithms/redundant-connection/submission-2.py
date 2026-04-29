class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph_hash = defaultdict(list)

        for e in edges:
            s, t = e
            graph_hash[s].append(t)
            graph_hash[t].append(s)

        # check loop
        loop_list = []
        parent_visited = []
        def dfs(val, visited, prev):
            nonlocal loop_list
            # print(val)
            print(visited)
            if val in visited:
                print("LOOP")
                loop_list = visited.copy()
                return False

            parent_visited.append(val)
            for neighbor in graph_hash[val]:
                if neighbor == prev:
                    continue
                visited.append(val)

                dfs(neighbor, visited, val)

                visited.pop()
            return True

        print(graph_hash)
        for val, _ in graph_hash.items():
            if val not in parent_visited:
                print(val)
                dfs(val, [], -1)
        
        print(loop_list)
        # generate pair from loop_list
        pair = []
        for i in range(len(loop_list) - 1):
            pair.append([loop_list[i], loop_list[i + 1]])
            pair.append([loop_list[i + 1], loop_list[i]])
        pair.append([loop_list[0], loop_list[len(loop_list) - 1]])
        pair.append([loop_list[len(loop_list) - 1], loop_list[0]])

        for i in range(len(edges) - 1, 0, -1):
            if edges[i] in pair:
                return edges[i]

