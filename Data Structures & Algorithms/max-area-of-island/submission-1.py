class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        res = 0

        is_visited = [[False if grid[r][c] == 1 else True for c in range(col_len)] for r in range(row_len)]
        print(is_visited)
        def markIslandVisited(row, col):
            print(row, col)
            # boundary
            if row < 0 or row >= row_len or col < 0 or col >= col_len:
                return 0

            if is_visited[row][col]:
                return 0

            # mark visited    
            is_visited[row][col] = True
            
            total_area = (1 + 
                # top 
                markIslandVisited(row - 1, col) + 
                # right
                markIslandVisited(row, col + 1) +
                # bottom
                markIslandVisited(row + 1, col) +
                # left
                markIslandVisited(row, col - 1))

            return total_area
            
        for cur_r in range(row_len):
            for cur_l in range(col_len):
                print(f"[NEXT] {cur_r} {cur_l}")
                if not is_visited[cur_r][cur_l] and grid[cur_r][cur_l] != 0:
                    res = max(res, markIslandVisited(cur_r, cur_l))
        
        return res