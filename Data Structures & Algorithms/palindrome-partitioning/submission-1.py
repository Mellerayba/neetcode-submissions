class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        candidate = []
        k=0
        def dfs(k):
            if k >= len(s):
                res.append(candidate.copy())
                return
            for end in range(k + 1, len(s) + 1):
                piece = s[k:end]
                if piece == piece[::-1]:               
                    candidate.append(piece)  
                    dfs(end)                
                    candidate.pop()          
                    
        
        dfs(0)
        return res