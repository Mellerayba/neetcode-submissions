class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}
        return(self.step(len(cost),cost,self.memo))

    def step(self, i, cost,memo):
        if i in self.memo:
            return self.memo[i]
        if i <= 1:
            return 0
        result = min(self.step(i-1,cost,memo)+ cost[i-1], self.step(i-2,cost,memo) + cost[i-2])
        self.memo[i] = result
        return result
        
