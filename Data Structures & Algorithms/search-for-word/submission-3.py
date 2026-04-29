class Solution:
    def solveq(self, board, word, start_row, start_col):
        visited = {}
        queue = deque([[start_row, start_col, 0]])
        substr = ""

        while len(queue) > 0:
            cur_row, cur_col, level = queue.popleft()

            if level >= len(word):
                break

            # overflow
            if cur_row >= len(board) or\
                cur_row < 0 or\
                cur_col < 0 or\
                cur_col >= len(board[0]):
                continue
            
            # is visited
            if f'{cur_row}_{cur_col}' in visited:
                continue
            
            print(visited)
            print(board[cur_row][cur_col], cur_row, cur_col, level)

            if board[cur_row][cur_col] == word[level]:
                substr += board[cur_row][cur_col]
                print(substr)
                if level == len(word) - 1:
                    return True
                # add top
                queue.append([cur_row - 1, cur_col, level + 1])
                # add left
                queue.append([cur_row, cur_col - 1, level + 1])
                # add right
                queue.append([cur_row, cur_col + 1, level + 1])
                # add bottom
                queue.append([cur_row + 1, cur_col, level + 1])

                visited[f'{cur_row}_{cur_col}'] = True
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = {}
        def solve(board, word, cur_row, cur_col, level):
            if level == len(word):
                return True

            # overflow
            if cur_row >= len(board) or\
                cur_row < 0 or\
                cur_col < 0 or\
                cur_col >= len(board[0]):
                return False
            
            # is visited
            if f'{cur_row}_{cur_col}' in visited:
                return False

            # is not the same as word
            if board[cur_row][cur_col] != word[level]:
                return False

            visited[f'{cur_row}_{cur_col}'] = True
            res = (solve(board, word, cur_row - 1, cur_col, level + 1) or
                    solve(board, word, cur_row + 1, cur_col, level + 1) or
                    solve(board, word, cur_row, cur_col - 1, level + 1) or
                    solve(board, word, cur_row, cur_col + 1, level + 1))
            del visited[f'{cur_row}_{cur_col}']
            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                is_found = solve(board, word, row, col, 0)
                if is_found:
                    return True
        return False

        