class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDic = {}
        retList = []
        for item in strs:
            temp = ""
            temp = temp.join(sorted(item))
            if temp not in wordDic:
                wordDic[temp] = [item]
            else:
                wordDic.get(temp).append(item)

        for anagram in wordDic:
            retList.append(wordDic[anagram])

        return retList  
            
        






        return [[]]
