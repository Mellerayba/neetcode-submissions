class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        start = 0
        end = len(nums)-1
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0-nums[i]
            start = i+1
            while start < end:
                if start == i:
                    continue
                if end == i:
                    continue
                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    temp = [nums[i],nums[start],nums[end]]
                    if temp not in triplets:
                        triplets.append(temp)
                    tempstart = start
                    tempend = end 
                    while start < end and nums[start] == nums[tempstart]:
                        start += 1
                    while start < end and nums[end] == nums[tempend]:
                        end -= 1
            end = len(nums)-1
        
        return triplets


        