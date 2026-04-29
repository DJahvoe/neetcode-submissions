class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph_hash = defaultdict(list)
        for s, t, c in flights:
            graph_hash[s].append((t, c))

        # best cost to reach dst using up to k+1 edges
        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        # (cumulative_cost, current_node, used_edges)
        min_heap = [(0, src, 0)]
        while min_heap:
            cost, node, used = heapq.heappop(min_heap)

            # if target found at minimum, return immediately
            if node == dst:
                return dist[dst][used]

            # if edge more than allowed, skip
            if used > k:
                continue

            # add neighbor
            for n_target, n_cost in graph_hash[node]:
                total_cost = n_cost + cost
                if total_cost < dist[n_target][used + 1]:
                    dist[n_target][used + 1] = total_cost
                    heapq.heappush(min_heap, (total_cost, n_target, used + 1))
            
        return -1
        
