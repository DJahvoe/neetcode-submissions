class Solution:
    def is_border(self, row, col, ROWS, COLS):
        return row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1

    def is_overflow(self, row, col, ROWS, COLS):
        return row < 0 or row >= ROWS or col < 0 or col >= COLS

    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        stay_circle_set = set()
        circle_q = deque([])


        # track circle on border
        for r in range(ROWS):
            for c in range(COLS):
                if self.is_border(r, c, ROWS, COLS) and board[r][c] == "O":
                    stay_circle_set.add((r, c))
                    circle_q.append((r, c))
        print(stay_circle_set)


        # bfs, check if neighboring cell is also circle, then track what needs to stay circle
        is_visited = set()
        while circle_q:
            r, c = circle_q.popleft()
            
            if(self.is_overflow(r, c, ROWS, COLS) or
                (r, c) in is_visited or
                board[r][c] == "X"):
                continue

            if(board[r][c] == "O"):
                stay_circle_set.add((r, c))

            is_visited.add((r, c))
            # up
            circle_q.append((r - 1, c))
            # down
            circle_q.append((r + 1, c))
            # left
            circle_q.append((r, c - 1))
            # right
            circle_q.append((r, c + 1))
            
        # convert all to X, except the one in stay_circle_set
        for r in range(ROWS):
            for c in range(COLS):
                if not ((r, c) in stay_circle_set):
                    board[r][c] = "X"