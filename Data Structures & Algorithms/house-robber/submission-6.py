class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        return self.step(0,nums,mem)
    def step(self,i,nums,mem):
        if i in mem:
            return mem[i]
        if i >= len(nums):
            return 0

            
        result = max(nums[i] + self.step(i+2,nums,mem), self.step(i+1,nums,mem))
        mem[i] = result 

        return result