class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        candidate = []
        free = nums.copy()

        def dfs(free):
            if len(free) == 0:
                res.append(candidate.copy())
                return
            for item in free[:]:
                candidate.append(item)
                free.remove(item)
                dfs(free)
                free.append(item)
                candidate.pop()

            
            return
        dfs(free)
        return res

            