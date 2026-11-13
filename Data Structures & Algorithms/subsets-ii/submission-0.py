class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        nums = sorted(nums)
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            current = i
            dfs(i+1)
            subset.pop()
            while i < len(nums) and nums[i] == nums[current]:
                i += 1
            dfs(i)
            return
        
        dfs(0)
        return res