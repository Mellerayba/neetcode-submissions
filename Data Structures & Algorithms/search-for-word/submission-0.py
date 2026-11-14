class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        candidate = ''
        def dfs(i,j,k):
            if k == len(word):
                return True
            if i >= len(board) or j >= len(board[0]) or j < 0 or i < 0:
                return False
            
            if board[i][j] != word[k] or board[i][j] == '-':
                return False
            
            k += 1
            temp = board[i][j]
            board[i][j] = '-'
            up = dfs(i-1,j,k)
            down = dfs(i+1,j,k)
            left = dfs(i,j-1,k)
            right = dfs(i,j+1,k)
            board[i][j] = temp

            return (up or down or left or right)
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp = dfs(i,j,0)
                if temp:
                    return True
        return False
