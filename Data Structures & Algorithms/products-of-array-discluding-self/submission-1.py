from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = reduce(lambda x, y: x * y, nums)
        retList=[]
        for item in nums:
            if item == 0:
                temp = nums.copy()
                temp.remove(0)
                retList.append(reduce(lambda x, y: x * y, temp))
            else:
                retList.append(total//item)
        return retList 
        