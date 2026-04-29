class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph_hash = defaultdict(list)
        tickets.sort()

        # create graph
        for src, trg in tickets:
            graph_hash[src].append(trg)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in graph_hash:
                return False
            
            temp = list(graph_hash[src])
            for i, v in enumerate(temp):
                # backtrack path
                graph_hash[src].pop(i)
                res.append(v)
                if dfs(v): return True
                graph_hash[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")

        return res
                

        