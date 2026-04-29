class Solution:
    def isHorizontalValid(self, board):
        for row in board:
            horizontal_set = set()
            for num in row:
                if num == '.':
                    continue
                if num in horizontal_set:
                    print("Horizontal Invalid")
                    return False
                horizontal_set.add(num)
        print("Horizontal Valid")
        return True

    def isVerticalValid(self, board):
        for col in range(len(board)):
            vertical_set = set()
            for row in range(len(board)):
                num = board[row][col]
                if num == '.':
                    continue
                if num in vertical_set:
                    print("Vertical Invalid")
                    return False
                vertical_set.add(num)
        print("Vertical Valid")
        return True

    def isSquareValid(self, board):
        for row_start in range(0, len(board), 3):
            for col_start in range(0, len(board), 3):
                square_set = set()
                for i in range(3):
                    for j in range(3):
                        num = board[row_start + i][col_start + j]
                        if num == '.':
                            continue
                        if num in square_set:
                            print("Square Invalid")
                            return False
                        square_set.add(num)
        print("Square Valid")
        return True

    def isValidSudoku(self, board):
        return self.isHorizontalValid(board) and self.isVerticalValid(board) and self.isSquareValid(board)
