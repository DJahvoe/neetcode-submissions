from typing import List, Tuple, Iterable
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Return the earliest time t at which we can travel from (0,0) to (n-1,n-1),
        moving 4-directionally, where the 'time so far' is defined as the maximum
        elevation we have stepped on along the path (minimize this maximum).
        """
        n = len(grid)
        target = (n - 1, n - 1)

        # Min-heap of states prioritized by the smallest "time so far".
        # "time so far" = max elevation encountered along the path to (r, c).
        heap: List[Tuple[int, int, int]] = [(grid[0][0], 0, 0)]

        # Visited set so each cell is finalized once (Dijkstra property).
        visited = set([(0, 0)])

        while heap:
            time_so_far, r, c = heapq.heappop(heap)

            # If we pop the target, this is the optimal (minimal) time by Dijkstra's invariant.
            if (r, c) == target:
                return time_so_far

            for nr, nc in self._neighbors(r, c, n):
                if (nr, nc) in visited:
                    continue
                visited.add((nr, nc))

                # To step into (nr, nc), water must be at least grid[nr][nc].
                # Our new path's max elevation is the max of current time and that cell's height.
                next_time = max(time_so_far, grid[nr][nc])
                heapq.heappush(heap, (next_time, nr, nc))

        # Problem guarantees connectivity under some t, so we should never get here.
        raise RuntimeError("Unreachable state")

    # ---- Helper utilities ----

    @staticmethod
    def _neighbors(r: int, c: int, n: int) -> Iterable[Tuple[int, int]]:
        """Yield 4-directional in-bounds neighbors of (r, c) on an n x n grid."""
        if r + 1 < n: yield (r + 1, c)
        if r - 1 >= 0: yield (r - 1, c)
        if c + 1 < n: yield (r, c + 1)
        if c - 1 >= 0: yield (r, c - 1)
