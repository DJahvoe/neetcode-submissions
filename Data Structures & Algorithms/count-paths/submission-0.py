class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row, column = m, n
        paths = []
        for r in range(row):
            temp = []
            for c in range(column):
                temp.append(0)
            paths.append(temp)
            
        for r in range(row - 1, -1, -1):
            for c in range(column - 1, -1, -1):
                bottom_sum = 0
                right_sum = 0
                if r + 1 == row:
                    paths[r][c] = 1
                    continue
                else:
                    bottom_sum += paths[r + 1][c]

                if c + 1 == column:
                    paths[r][c] = 1
                    continue
                else:
                    right_sum += paths[r][c + 1]
                paths[r][c] = bottom_sum + right_sum
                print("{} {} = {}".format(r, c, paths[r][c]))
                print(paths)
        return paths[0][0]
