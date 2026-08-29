class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        retList = []
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
  
        dsc = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
        for i in range(k):
            retList.append(list(dsc)[i])

        return retList
        

        