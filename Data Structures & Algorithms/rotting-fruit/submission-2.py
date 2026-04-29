class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        res = 0
        # init
        for row_i in range(0, len(grid)):
            for col_i in range(0, len(grid[0])):
                if grid[row_i][col_i] == 2:
                    q.append((row_i, col_i, 0))

        
        while q:
            print(q)
            row, col, minute_count = q.popleft()
            res = max(res, minute_count)
            print(row, col, minute_count)

            # up
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                print("UP is 1")
                q.append((row - 1, col, minute_count + 1))
                grid[row - 1][col] = 2
            # down
            if row + 1 < len(grid) and grid[row + 1][col] == 1:
                print("DOWN is 1")
                q.append((row + 1, col, minute_count + 1))
                grid[row + 1][col] = 2
            # left
            if col - 1 >= 0 and grid[row][col - 1] == 1:
                print("LEFT is 1")
                q.append((row, col - 1, minute_count + 1))
                grid[row][col - 1] = 2
            # right
            if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                print("RIGHT is 1")
                q.append((row, col + 1, minute_count + 1))
                grid[row][col + 1] = 2
        for row in grid:
            if 1 in row:
                return -1
        return res
        
