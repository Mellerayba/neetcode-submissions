class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        start = 0
        end = len(nums)-1
        for i in range(len(nums)-1):
            target = 0-nums[i]
            start = i+1
            for j in range(len(nums) -i -1):
                if start == i:
                    continue
                if end == i:
                    continue
                if start == end:
                    continue
                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    temp = [nums[i],nums[start],nums[end]]
                    if temp not in triplets:
                        triplets.append(temp)
                    start+=1
            end = len(nums)-1
        
        return triplets


        