class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph_hash = defaultdict(list)
        cost_hash = {}
        min_heap = []

        # create adjacency list graph
        for t in times:
            source, target, time = t
            graph_hash[source].append((target, time))

        # track cost from first node
        heapq.heappush(min_heap, (0, k))

        visited = set()
        while min_heap:
            smallest_cost, node = heapq.heappop(min_heap)
            if node in cost_hash:
                continue
            cost_hash[node] = smallest_cost
            
            # check neighbor
            for edge in graph_hash[node]:
                neighbor, time = edge
                heapq.heappush(min_heap, (smallest_cost + time, neighbor))
                
        
        print(cost_hash)
        for i in range(1, n + 1):
            if i not in cost_hash:
                return -1
        
        res = 0
        for _, val in cost_hash.items():
            res = max(res, val)
        return res

        