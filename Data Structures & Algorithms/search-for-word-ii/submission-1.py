class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def solve(board, word, cur_row, cur_col, level, visited):
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

            temp = board[cur_row][cur_col]
            board[cur_row][cur_col] = "."
            visited[f'{cur_row}_{cur_col}'] = True
            res = (solve(board, word, cur_row - 1, cur_col, level + 1, visited) or
                    solve(board, word, cur_row + 1, cur_col, level + 1, visited) or
                    solve(board, word, cur_row, cur_col - 1, level + 1, visited) or
                    solve(board, word, cur_row, cur_col + 1, level + 1, visited))
            del visited[f'{cur_row}_{cur_col}']
            board[cur_row][cur_col] = temp
            return res

        res = []
        for word in words:
            visited = {}
            is_break = False
            for row in range(len(board)):
                for col in range(len(board[0])):
                    is_found = solve(board, word, row, col, 0, visited)
                    if is_found:
                        res.append(word)
                        break
                else:
                    continue
                break
            
        return res