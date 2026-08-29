class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                temp = prices[r] - prices[l]
                if temp>profit:
                    profit = temp
            else:
                l = r
            r += 1
        return profit