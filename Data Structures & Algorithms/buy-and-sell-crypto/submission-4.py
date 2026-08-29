class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1,0,-1):
            if prices[i]-min(prices[:i]) > profit:
                profit = prices[i]-min(prices[:i])
        return profit