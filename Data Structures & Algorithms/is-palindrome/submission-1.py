class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [value for value in s if value.isalpha() or value.isnumeric()]
        a = s.copy()
        a.reverse()
        if a == s:
            return True
        return False