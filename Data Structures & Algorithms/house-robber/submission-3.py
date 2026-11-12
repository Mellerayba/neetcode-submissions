class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        return self.step(0,nums,mem)
    def step(self,i,nums,mem):
        if i == len(nums)-2:
            return max(nums[i],nums[i+1])
        elif i == len(nums)-1:
            return nums[i]
        if i in mem:
            return mem[i]
            
        result = max(nums[i] + self.step(i+2,nums,mem), self.step(i+1,nums,mem))
        mem[i] = result 

        return result