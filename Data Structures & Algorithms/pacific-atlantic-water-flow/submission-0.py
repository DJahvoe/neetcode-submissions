class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visit, prev_height):
            if((r, c) in visit or
                r < 0 or
                c < 0 or
                r == ROWS or
                c == COLS or
                heights[r][c] < prev_height):
                return
            visit.add((r,c))
            # up
            dfs(r + 1, c, visit, heights[r][c])
            # down
            dfs(r - 1, c, visit, heights[r][c])
            # right
            dfs(r, c + 1, visit, heights[r][c])
            # left
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            # traverse pacific top
            dfs(0, c, pac, heights[0][c])

            # traverse atlantic bottom
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            # traverse pacific left
            dfs(r, 0, pac, heights[r][0])

            # traverse atlantic right
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # find if point reachable from both
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


        
