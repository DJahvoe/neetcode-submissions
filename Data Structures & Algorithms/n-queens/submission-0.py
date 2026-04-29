class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(cur_row):
            if cur_row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for cur_col in range(n):
                if cur_col in col or\
                    (cur_row + cur_col) in pos_diag or\
                    (cur_row - cur_col) in neg_diag:
                    continue
                
                col.add(cur_col)
                pos_diag.add(cur_row + cur_col)
                neg_diag.add(cur_row - cur_col)
                board[cur_row][cur_col] = "Q"

                backtrack(cur_row + 1)

                col.remove(cur_col)
                pos_diag.remove(cur_row + cur_col)
                neg_diag.remove(cur_row - cur_col)
                board[cur_row][cur_col] = "."
        
        backtrack(0)
        return res
