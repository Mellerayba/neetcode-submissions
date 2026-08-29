class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            res += str(len(item)) + "#" + item
        
        return res

    def decode(self, s: str) -> List[str]:
        pointer = 0
        retList = []

        while pointer < len(s):
            j = s.find("#", pointer)
            length = int(s[pointer:j])
            retList.append(s[j+1:j + 1 + length])
            pointer = j + 1 + length
        return retList
