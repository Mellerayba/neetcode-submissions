class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_count = max(max_count, self.dfs(i,j,grid))
        return max_count

    def dfs(self,i,j,grid):
        if i >= len(grid) or i < 0:
            return 0
        if j >= len(grid[0]) or j < 0:
            return 0

        if grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        check = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        count = 1
        for item in check:
            count+= self.dfs(item[0],item[1],grid)
        
        return count
