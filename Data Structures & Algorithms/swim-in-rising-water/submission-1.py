import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        # (time so far, r, c) where time is the max elevation seen on the path to (r, c)
        heap = [(grid[0][0], 0, 0)]
        seen = set([(0, 0)])
        
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return t  # the earliest time water is high enough to have connected a path here
            
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    # time to step into (nr, nc) is the max of current time and that cell's elevation
                    nt = max(t, grid[nr][nc])
                    heapq.heappush(heap, (nt, nr, nc))
