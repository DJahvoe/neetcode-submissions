class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # generate graph
        graph_hash = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                # calculate distance
                d = abs(x1 - x2) + abs(y1 - y2)

                # if self, skip
                if d == 0:
                    continue
                graph_hash[i].append([d, j])
                graph_hash[j].append([d, i])

        min_heap = [[0, 0]]
        res = 0
        visited = set()
        # add all neighbors from root
        while len(visited) < len(points):
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for n_cost, n_i in graph_hash[i]:
                if n_i not in visited:
                    heapq.heappush(min_heap, [n_cost, n_i])
        
        return res

        