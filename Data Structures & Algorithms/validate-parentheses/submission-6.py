class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        opening = "({["
        pairs = {"(":")","{":"}","[":"]"}
        for i in s:
            if i in opening:
                queue.append(i)
            else:
                if not queue:
                    return False
                if pairs[queue.pop()] != i:
                    return False
        if queue:
            return False
        return True