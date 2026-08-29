class Solution:
    def groupAnagrams(self, strs):
        wordDic = {}
        for item in strs:
            key = "".join(sorted(item))
            if key not in wordDic:
                wordDic[key] = []
            wordDic[key].append(item)
        return list(wordDic.values())
            
        







