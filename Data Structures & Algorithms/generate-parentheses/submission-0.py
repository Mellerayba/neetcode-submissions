class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        open_b = 0
        close_b = 0
        candidate = ''
        
        def dfs(candidate, open_b,close_b):
            if len(candidate) >= 2 * n:
                res.append(candidate)
                return
            if open_b < n:
                dfs(candidate + '(', open_b + 1,close_b)
                
            if close_b < open_b:
                dfs(candidate + ')', open_b,close_b + 1)
            return
        dfs(candidate, open_b,close_b)
        return res