class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        res = 0

        is_visited = [[False if grid[r][c] == "1" else True for c in range(col_len)] for r in range(row_len)]
        def markIslandVisited(row, col):
            print(row, col)
            # boundary size
            if row < 0 or row >= row_len or col < 0 or col >= col_len:
                return
            # boundary visited
            if is_visited[row][col]:
                return

            # mark visited    
            is_visited[row][col] = True

            # top
            markIslandVisited(row - 1, col)

            # right
            markIslandVisited(row, col + 1)

            # bottom
            markIslandVisited(row + 1, col)

            # left
            markIslandVisited(row, col - 1)
            
        for cur_r in range(row_len):
            for cur_l in range(col_len):
                print(f"[NEXT] {cur_r} {cur_l}")
                if not is_visited[cur_r][cur_l] and grid[cur_r][cur_l] != "0":
                    res += 1
                    markIslandVisited(cur_r, cur_l)
                is_visited[cur_r][cur_l] = True
        
        return res