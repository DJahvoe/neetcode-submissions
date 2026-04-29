class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        any_zero_first_row = False
        any_zero_first_col = False
        # mark zero to top-row and left-column
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        any_zero_first_row = True
                    if c == 0:
                        any_zero_first_col = True

                    # mark the first row for column c to 0
                    matrix[0][c] = 0
                    if r > 0:
                        # mark the first column for row r to 0
                        matrix[r][0] = 0
        
        # update zero, based on first row and first column
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # if top-left = 0, set whole first row to 0, set whole first column to 0
        if any_zero_first_row:
            for c in range(COLS):      # zero FIRST ROW
                matrix[0][c] = 0

        if any_zero_first_col:
            for r in range(ROWS):      # zero FIRST COLUMN
                matrix[r][0] = 0