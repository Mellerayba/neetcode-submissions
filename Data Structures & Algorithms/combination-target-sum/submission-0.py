class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        total = 0
        def dfs(i):
            if i >= len(nums):
                if sum(combination) == target:
                    res.append(combination.copy())
                return
            if sum(combination) > target:
                return
            combination.append(nums[i])
            dfs(i)
            combination.pop()
            dfs(i+1)
            return
        
        dfs(0)
        return res