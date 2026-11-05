class Solution:
    def climbStairs(self, n: int) -> int:
        self.seen = {1:1,2:2}
        return self.climb(n)
    
    def climb(self, n):
        if n < 3:
            return n
        pos = max(self.seen) + 1
        while pos < n:
            self.seen[pos] = self.seen[pos-2] + self.seen[pos-1]
            pos += 1
        res = self.seen.get(n-1) + self.seen.get(n-2)
        self.seen[n] = res
        return res
        
