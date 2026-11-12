class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mem1 = {}
        mem2 = {}
        one = nums[1:]
        two = nums[:-1]
        return max(self.step(0,one,mem1),self.step(0,two,mem2))
    def step(self,i,nums,mem):
        if i in mem:
            return mem[i]
        if i >= len(nums):
            return 0            
        result = max(nums[i] + self.step(i+2,nums,mem), self.step(i+1,nums,mem))
        mem[i] = result 

        return result