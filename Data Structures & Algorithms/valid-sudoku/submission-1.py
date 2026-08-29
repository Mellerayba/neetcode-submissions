class Solution:
    def isValidSudoku(self, board):
        rows = {i: [] for i in range(9)}
        cols = {i: [] for i in range(9)}
        squares = {}  # key: (row//3, col//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                box = (r // 3, c // 3)
                
                if (val in rows[r] or
                    val in cols[c] or
                    val in squares.get(box, [])):
                    return False
                
                rows[r].append(val)
                cols[c].append(val)
                squares.setdefault(box, []).append(val)

        return True


        