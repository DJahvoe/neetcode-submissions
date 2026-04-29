class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph_hash = {i: [] for i in range(n)}
        res = 0

        # create graph
        for e in edges:
            s, t = e
            # undirected graph
            graph_hash[s].append(t)
            graph_hash[t].append(s)

        visited = set()
        for k, v in graph_hash.items():
            if k in visited:
                continue

            # bfs
            q = deque([(k, -1)])
            while q:
                val, prev = q.popleft()
                visited.add(val)
                for neighbor in graph_hash[val]:
                    if neighbor == prev or neighbor in visited:
                        continue
                    q.append((neighbor, val))
            res += 1
        return res