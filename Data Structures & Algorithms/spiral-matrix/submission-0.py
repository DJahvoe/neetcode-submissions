class Solution:
    def isFrontVisited(self, matrix, r, c):
        is_front_visited = matrix[r][c] == 101
        if is_front_visited:
            print("IS FRONT VISITED")
        return is_front_visited
            
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        direction = 0
        r, c = 0, 0
        res = []
        for i in range(ROWS * COLS):
            res.append(matrix[r][c])
            matrix[r][c] = 101   # mark visited
            
            # right
            if direction == 0:
                if c + 1 >= COLS or self.isFrontVisited(matrix, r, c + 1):
                    direction = 1     # turn down
                else:
                    c += 1            # move right
                    continue

            # bottom
            elif direction == 1:
                if r + 1 >= ROWS or self.isFrontVisited(matrix, r + 1, c):
                    direction = 2     # turn left
                else:
                    r += 1            # move down
                    continue

            # left
            elif direction == 2:
                if c - 1 < 0 or self.isFrontVisited(matrix, r, c - 1):
                    direction = 3     # turn up
                else:
                    c -= 1            # move left
                    continue

            # top
            elif direction == 3:
                if r - 1 < 0 or self.isFrontVisited(matrix, r - 1, c):
                    direction = 0     # turn right
                else:
                    r -= 1            # move up
                    continue

            # direction changed — move one step in new direction
            if direction == 0:
                c += 1
            elif direction == 1:
                r += 1
            elif direction == 2:
                c -= 1
            else:
                r -= 1
            
        return res
                