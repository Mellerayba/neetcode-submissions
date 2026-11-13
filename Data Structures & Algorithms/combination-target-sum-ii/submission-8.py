class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        candidates = sorted(candidates)
        def dfs(i):
            if i >= len(candidates):
                if sum(combination) == target:
                    res.append(combination.copy())
                return
            if sum(combination) > target:
                return
            combination.append(candidates[i])
            current = i
            dfs(i+1)
            combination.pop()
            while i < len(candidates) and candidates[i] == candidates[current]:
                i += 1
            dfs(i)
            return
        
        dfs(0)
        return res