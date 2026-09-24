class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r 
        while l <= r:
            k = l + ((r - l) // 2)
            hours = sum((pile + k - 1) // k for pile in piles)
            if hours <= h:
                best = k       
                r = k - 1   
            else:
                l = k + 1
        return best