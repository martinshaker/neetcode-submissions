class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:       
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            seen = set()
            for i in range(cols):
                if board[r][i] == '.':
                    continue
                if board[r][i] in seen:
                    return False
                seen.add(board[r][i])

        for c in range(cols):
            seen = set()
            for i in range(cols):
                if board[i][c] == '.':
                    continue
                if board[i][c] in seen:
                    return False
                seen.add(board[i][c])

        for square in range(rows):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True




            
