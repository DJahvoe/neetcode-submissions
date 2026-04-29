class Solution:
    def islandsAndTreasure(self, grid) -> None:
        row_size = len(grid)
        col_size = len(grid[0])
        INF = 2147483647
        
        queue = deque([])

        is_visited = set()

        def bfs():
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while queue:
                row, col, distance = queue.popleft()
                
                if 0 < grid[row][col] <= INF:
                    grid[row][col] = min(grid[row][col], distance)

                is_visited.add((row, col))

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < row_size and 0 <= new_col < col_size and grid[new_row][new_col] != -1 and (new_row, new_col) not in is_visited:
                        queue.append((new_row, new_col, distance + 1))
        
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == -1:
                    continue
                if grid[row][col] == 0:
                    queue.append((row, col, 0))
                    is_visited = set()
                    bfs()
