class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""

        def expand(l, r):
            # grow outwards while in bounds and the ends match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]      # the loop overshot by one on each side

        for i in range(len(s)):
            odd = expand(i, i)         # centre is a character
            even = expand(i, i + 1)    # centre is between two characters
            if len(odd) > len(best):
                best = odd
            if len(even) > len(best):
                best = even

        return best