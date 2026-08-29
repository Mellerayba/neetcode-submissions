class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = 0
        s1 = sorted(s1)
        for i in range(len(s1),len(s2)+1):
            temp = sorted(s2[count:i])
            if temp == s1:
                return True
            count += 1
        return False