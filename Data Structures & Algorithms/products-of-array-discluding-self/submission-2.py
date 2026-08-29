from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = reduce(lambda x, y: x * y, nums)
        retList=[]
        zeros = nums.count(0)
        if zeros > 1:
            return [0] * len(nums)
        
        for item in nums:
            if item == 0:
                temp = nums.copy()
                temp.remove(0)
                retList.append(reduce(lambda x, y: x * y, temp))
            else:
                retList.append(total//item)
        return retList 
        